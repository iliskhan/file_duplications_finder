import os
from file import File
from utils import perf_timer
from multiprocessing.dummy import Pool
from multiprocessing.pool import ThreadPool

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

        pool: ThreadPool
        with Pool() as pool: 
            self.files.clear()
            for root, _, filenames in os.walk(self.path):
                files = pool.map(get_file, ((root, filename) for filename in filenames))
                self.files.extend(files)

    @perf_timer
    def get_duplicate_files(self):
        unique_files = {}
        for file in self.files:
            if file.hash in unique_files:
                unique_files[file.hash].append(file)
            else:
                unique_files[file.hash] = [file]
        return {k:v for k,v in unique_files.items() if len(v)>1}
