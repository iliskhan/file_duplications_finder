from ui import UI
from file_storage import FileStorage

class App:
    def __init__(self):
        self.ui = UI()

    def run(self):
        self.ui.root.mainloop()

if __name__ == '__main__':
    app = App()
    app.run()
