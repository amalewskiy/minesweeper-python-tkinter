from tkinter import Tk
from createMenu import CreateFrame


class MainApplication:
    def __init__(self, master):
        self.root = master
        self.menu = CreateFrame(self.root)
        self.menu.createMenuFrame()


if __name__ == '__main__':
    root = Tk()
    root.resizable(False, False)
    ox = root.winfo_screenwidth() / 2
    oy = root.winfo_screenheight() / 2
    root.geometry(f'+{int(ox - 150)}+{int(oy - 150)}')
    MainApplication(root)
    root.mainloop()
