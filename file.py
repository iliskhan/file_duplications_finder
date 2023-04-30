import os
import hashlib

class File:
    def __init__(self, path):
        self.path = path

    def get_size(self):
        return os.path.getsize(self.path)
    
    def get_creation_date(self):
        return os.path.getctime(self.path)
    
    def get_hash(self):
        hash_md5 = hashlib.md5()
        with open(self.path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
        
    def __eq__(self, other):
        return self.get_hash() == other.get_hash()
