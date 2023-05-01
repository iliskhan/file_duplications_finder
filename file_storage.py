import os
from file import File
from utils import perf_timer
from multiprocessing.dummy import Pool

class FileStorage:
    def __init__(self, path):
        self.path = path
        self.files = []

    @perf_timer
    def scan_files(self):
        def get_file(args):
            root, filename = args

            full_path = os.path.join(root, filename)
            relative_path = os.path.relpath(full_path, self.path)
            return File(full_path=full_path, relative_path=relative_path)

        with Pool() as pool:
            for root, _, files in os.walk(self.path):
                for file in pool.imap(get_file, [(root, filename) for filename in files]):
                    self.files.append(file)

    @perf_timer
    def get_duplicate_files(self):
        unique_files = {}
        for file in self.files:
            if file.hash in unique_files:
                unique_files[file.hash].append(file)
            else:
                unique_files[file.hash] = [file]
        return {k:v for k,v in unique_files.items() if len(v)>1}
