import json

class Settings:
    def __init__(self):
        self.path = "settings.json"
        self.data = {}
        self.load()

    def load(self):
        try:
            with open(self.path, "r") as file:
                self.data = json.load(file)
        except FileNotFoundError:
            self.save()

    def save(self):
        with open(self.path, "w") as file:
            json.dump(self.data, file)

    def get(self, key):
        return self.data.get(key)

    def set(self, key, value):
        self.data[key] = value
        self.save()
