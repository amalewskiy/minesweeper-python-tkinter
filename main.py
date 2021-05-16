from tkinter import Tk
from createMenu import CreateFrame


class MainApplication:
    def __init__(self, master):
        self.root = master
        self.menu = CreateFrame(self.root)
        self.menu.createMenuFrame()


if __name__ == "__main__":
    root = Tk()
    root.resizable(False, False)
    ox = root.winfo_screenwidth() / 2
    oy = root.winfo_screenheight() / 2
    root.geometry(f'+{int(ox - 400)}+{int(oy - 345)}')
    apk = MainApplication(root)
    root.mainloop()
