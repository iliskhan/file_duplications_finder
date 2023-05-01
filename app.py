from ui import UI
from file_storage import FileStorage

class App:
    def __init__(self):
        self.ui = UI()

    def run(self):
        try:
            self.ui.root.mainloop()
        except Exception as err:
            self.ui.log('ERROR: %s' % err)
            raise

if __name__ == '__main__':
    app = App()
    app.run()
