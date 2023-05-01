import os
import time
from file import File
from utils import perf_timer

class FileStorage:
    def __init__(self, path):
        self.path = path
        self.files = []

    @perf_timer
    def scan_files(self):
        for root, _, files in os.walk(self.path):
            for filename in files:
                full_path = os.path.join(root, filename)
                relative_path = os.path.relpath(full_path, self.path)
                file = File(full_path=full_path, relative_path=relative_path)
                self.files.append(file)

    @perf_timer
    def get_duplicate_files(self):
        unique_files = {}
        for file in self.files:
            if file.get_hash() in unique_files:
                unique_files[file.get_hash()].append(file)
            else:
                unique_files[file.get_hash()] = [file]
        return {k:v for k,v in unique_files.items() if len(v)>1}
