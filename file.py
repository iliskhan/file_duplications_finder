import os
import hashlib
import logging
from datetime import datetime

from utils import convert_unit


logger = logging.getLogger(__name__)

class File:
    def __init__(self, full_path, relative_path):
        self.path = full_path
        self.relative_path = relative_path
        self.size = self.get_size()
        self.human_readable_size = convert_unit(self.size)
        self.creation_date = self.get_creation_date()
        self.hash = self.get_hash()

    def get_size(self):
        try:
            return os.path.getsize(self.path)
        except OSError as e:
            logger.exception(e)
            raise

    def get_creation_date(self):
        try:
            return datetime.fromtimestamp(os.path.getctime(self.path)).replace(microsecond=0)
        except OSError as e:
            logger.exception(e)
            raise

    def get_hash(self):
        hash_md5 = hashlib.md5()
        try:
            with open(self.path, "rb") as f:
                for chunk in iter(lambda: f.read(64*1024), b""):
                    hash_md5.update(chunk)
        except OSError as e:
            logger.exception(e)
            raise
        return hash_md5.hexdigest()
        
    def delete(self):
        try:
            os.remove(self.path)
        except OSError as e:
            logger.exception(e)
            raise

    def __eq__(self, other):
        return self.hash == other.hash

    def __repr__(self):
        return f"File({self.path!r})"

    def __str__(self):
        return f"File({self.path!r})"

    def __hash__(self):
        return hash(self.path)

    def __lt__(self, other):
        return self.path < other.path

    def __gt__(self, other):
        return self.path > other.path

    def __le__(self, other):
        return self.path <= other.path

    def __ge__(self, other):
        return self.path >= other.path

