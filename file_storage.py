import os
from file import File

class FileStorage:
    def __init__(self, path):
        self.path = path
        self.files = []

    def scan_files(self):
        for root, dirs, files in os.walk(self.path):
            for filename in files:
                full_path = os.path.join(root, filename)
                self.files.append(File(full_path))

    def get_duplicate_files(self):
        unique_files = {}
        for file in self.files:
            if file.get_hash() in unique_files:
                unique_files[file.get_hash()].append(file)
            else:
                unique_files[file.get_hash()] = [file]
        return {k:v for k,v in unique_files.items() if len(v)>1}

    def delete_file(self, file):
        os.remove(file.path)
        self.files.remove(file)
