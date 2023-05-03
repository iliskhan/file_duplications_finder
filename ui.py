import os
import platform
import subprocess

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from file_storage import FileStorage

FOLDER_LABEL_TEXT = "Selected folder to scan:"

class UI:
    def __init__(self):
        self.files_ids = {}

        self.root = tk.Tk()
        self.root.title("Duplicate Files Finder")
        self.style = ttk.Style()

        self.style.theme_use('clam')

        self.file_storage = None

        self.content_frame = ttk.Frame(self.root, padding=20)
        self.content_frame.pack(fill=tk.BOTH, expand=True)

        self.folder_to_scan_label = ttk.Label(self.content_frame, text=FOLDER_LABEL_TEXT)
        self.folder_to_scan_label.pack(pady=10, anchor=tk.NW)

        self.select_folder_button = ttk.Button(self.content_frame, text="Select Folder", command=self.select_folder)
        self.select_folder_button.pack(side=tk.RIGHT)

        self.scan_files_button = ttk.Button(self.content_frame, text="Scan Files", command=self.scan_files, state=tk.DISABLED)
        self.scan_files_button.pack(pady=10, side=tk.RIGHT)

        self.delete_button = ttk.Button(self.content_frame, text="Delete Selected File", command=self.delete_file, state=tk.DISABLED)
        self.delete_button.pack(side=tk.RIGHT)

        self.create_duplicate_files_table()

        self.root.mainloop()

    def create_duplicate_files_table(self):
        columns = ("id", "hashsum", "name", "creation date", "size")
        self.duplicate_files_table = ttk.Treeview(self.content_frame, columns=columns, show="headings")

        self.duplicate_files_table_scrollbar_y = ttk.Scrollbar(self.content_frame, orient="vertical", command=self.duplicate_files_table.yview)
        self.duplicate_files_table_scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)

        self.duplicate_files_table_scrollbar_x = ttk.Scrollbar(self.content_frame, orient="horizontal", command=self.duplicate_files_table.xview)
        self.duplicate_files_table_scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)

        self.duplicate_files_table.configure(yscrollcommand=self.duplicate_files_table_scrollbar_y.set, xscrollcommand=self.duplicate_files_table_scrollbar_x.set)

        self.duplicate_files_table.heading("id", text="Id", command=lambda: self.sort_column("id"))
        self.duplicate_files_table.heading("hashsum", text="Hashsum", command=lambda: self.sort_column("hashsum"))
        self.duplicate_files_table.heading("name", text="Name", command=lambda: self.sort_column("name"))
        self.duplicate_files_table.heading("creation date", text="Creation date", command=lambda: self.sort_column("creation date"))
        self.duplicate_files_table.heading("size", text="Size", command=lambda: self.sort_column("size"))

        self.duplicate_files_table.column("id", width=20, stretch=True)
        self.duplicate_files_table.column("hashsum", width=100, stretch=True)
        self.duplicate_files_table.column("name", width=300, stretch=True)
        self.duplicate_files_table.column("creation date", width=100, stretch=True)
        self.duplicate_files_table.column("size", width=50, stretch=True)

        self.duplicate_files_table.bind("<Double-1>", self.on_tree_row_double_click)

        self.duplicate_files_table.bind("<Shift-Up>", self.shift_key_press)
        self.duplicate_files_table.bind("<Shift-Down>", self.shift_key_press)

        self.duplicate_files_table.pack(pady=10, expand=True, fill=tk.BOTH)

    def shift_key_press(self, event):
        tree = event.widget
        cur_item = tree.focus()

        # You need the next item, because you `"break"` standard behavior
        match event.keysym:
            case 'Up':
                next_item = tree.prev(cur_item)
            case 'Down':
                next_item = tree.next(cur_item)
            
        # Set the keyboard focus to the `next_item`
        tree.focus(next_item)

        if next_item in tree.selection():
            # If the item is already selected, deselect it
            tree.selection_remove(cur_item)
        else:
            # add both items to the selection
            tree.selection_add([cur_item, next_item])

        # Stop propagating this event to other handlers!
        return 'break'

    def on_tree_row_double_click(self, event):
        for item_id in self.duplicate_files_table.selection():
            file = self.files_ids[item_id]

        if platform.system() == 'Darwin':       # macOS
            subprocess.call(('open', file.path))
        elif platform.system() == 'Windows':    # Windows
            os.startfile(file.path)
        else:                                   # linux variants
            subprocess.call(('xdg-open', file.path))

    def sort_column(self, column, reverse=False):
        if column == "size":
            l = [(int(self.files_ids[k].size), k) for k in self.duplicate_files_table.get_children('')]
        elif column == "id":
            l = [(int(self.duplicate_files_table.set(k, column)), k) for k in self.duplicate_files_table.get_children('')]
        else:
            l = [(self.duplicate_files_table.set(k, column), k) for k in self.duplicate_files_table.get_children('')]
        
        l.sort(reverse=reverse)

        # rearrange items in sorted positions
        for index, (_, k) in enumerate(l):
            self.duplicate_files_table.move(k, '', index)

        # reverse sort next time
        self.duplicate_files_table.heading(column, command=lambda: self.sort_column(column, not reverse))

    def select_folder(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.file_storage = FileStorage(folder_path)
            self.scan_files_button.config(state=tk.NORMAL)
            self.folder_to_scan_label.config(text=f"{FOLDER_LABEL_TEXT} {folder_path}")

    def scan_files(self):
        self.file_storage.scan_files()
        duplicates = self.file_storage.get_duplicate_files()
        if duplicates:
            for item in self.duplicate_files_table.get_children():
                self.duplicate_files_table.delete(item)

            id_to_show = 1
            for hashsum, files in duplicates.items():
                default_selection = []
                for file in files:
                    values = (id_to_show, hashsum, file.relative_path, file.creation_date, file.human_readable_size)
                    id = self.duplicate_files_table.insert("", tk.END, values=values)
                    self.files_ids[id] = file
                    default_selection.append(id)
                    id_to_show += 1  
                
                self.duplicate_files_table.selection_add(default_selection[:-1])
            self.scan_files_button.config(state=tk.DISABLED)
            self.delete_button.config(state=tk.NORMAL)
        else:
            messagebox.showinfo("Duplicate Files Finder", "No Duplicate Files Found.")

    def delete_file(self):
        for item_id in self.duplicate_files_table.selection():
            file = self.files_ids.pop(item_id)
            file.delete()
            self.duplicate_files_table.delete(item_id)
        
        if not self.files_ids:
            self.delete_button.config(state=tk.DISABLED)
