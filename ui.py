import tkinter as tk
from tkinter import filedialog, messagebox
from file_storage import FileStorage

class UI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Duplicate Files Finder")

        self.file_storage = None

        self.label1 = tk.Label(self.root, text="Select Folder to Scan:")
        self.label1.pack(pady=10)

        self.select_folder_button = tk.Button(self.root, text="Select Folder", command=self.select_folder)
        self.select_folder_button.pack()

        self.scan_files_button = tk.Button(self.root, text="Scan Files", command=self.scan_files, state=tk.DISABLED)
        self.scan_files_button.pack(pady=10)

        self.duplicate_files_listbox = tk.Listbox(self.root, width=50)
        self.duplicate_files_listbox.pack(pady=10)

        self.delete_button = tk.Button(self.root, text="Delete Selected File", command=self.delete_file, state=tk.DISABLED)
        self.delete_button.pack()

        self.root.mainloop()

    def select_folder(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.file_storage = FileStorage(folder_path)
            self.scan_files_button.config(state=tk.NORMAL)

    def scan_files(self):
        self.file_storage.scan_files()
        duplicates = self.file_storage.get_duplicate_files()
        if duplicates:
            for hashsum, files in duplicates.items():
                self.duplicate_files_listbox.insert(tk.END, f"{hashsum}:")
                for file in files:
                    self.duplicate_files_listbox.insert(tk.END, f"    {file.path}")
                self.duplicate_files_listbox.insert(tk.END, "")
            self.delete_button.config(state=tk.NORMAL)
        else:
            messagebox.showinfo("Duplicate Files Finder", "No Duplicate Files Found.")

    def delete_file(self):
        selected_indices = self.duplicate_files_listbox.curselection()
        if selected_indices:
            selected_file = self.duplicate_files_listbox.get(selected_indices[0])
            self.file_storage.delete_file(selected_file)
            self.duplicate_files_listbox.delete(selected_indices[0])
            messagebox.showinfo("Duplicate Files Finder", "File Deleted Successfully.")
        else:
            messagebox.showinfo("Duplicate Files Finder", "Please Select a File to Delete.")
