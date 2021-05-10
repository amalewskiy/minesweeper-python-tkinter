from usefulFunctions import clearMenuWindow, clearGameWindow, createField, howManyMines, howManyZero, whatIsColor, \
    openMyAccount
from tkinter import Label, Button, Entry, END, StringVar, messagebox


class CreateFrame:
    def __init__(self, root):
        self.root = root
        self.buttonInRows = 0
        self.buttonInColumns = 0
        self.minesInFiled = 0
        self.minesInFiledCopy = 0
        self.countClick = 0
        self.origColor = 0
        self.allBtn = []
        self.minesWeeperField = []
        self.beginnerButton = Button()
        self.amountMinesLabel = Label()

    def rightButton(self, numRow, numCol):
        if self.allBtn[numRow - 1][numCol]["bg"] == "green":
            self.minesInFiledCopy += 1
            self.countClick -= 1
            self.allBtn[numRow - 1][numCol]["bg"] = self.origColor

        elif self.allBtn[numRow - 1][numCol]['text'] == '     ' and \
                self.allBtn[numRow - 1][numCol]["state"] == "normal":
            self.allBtn[numRow - 1][numCol]["bg"] = "green"
            self.minesInFiledCopy -= 1
            self.countClick += 1
        self.amountMinesLabel.configure(text=f'{self.minesInFiledCopy}')
        self.isWinning()

    def isWinning(self):
        if self.countClick == self.buttonInRows * self.buttonInColumns:
            Label(self.root, text="You won!", bg='gainsboro').grid(columnspan=self.buttonInColumns)
            for i in range(0, self.buttonInRows):
                for j in range(self.buttonInColumns):
                    self.allBtn[i][j]["state"] = "disabled"

    def identifyButton(self, numRow, numCol):
        if self.allBtn[numRow - 1][numCol]['bg'] != 'green':
            if self.minesWeeperField[numRow][numCol + 1] == 1:
                for i in range(1, self.buttonInRows + 1):
                    for j in range(self.buttonInColumns):
                        if self.minesWeeperField[i][j + 1] == 1 and self.allBtn[i - 1][j]["bg"] != "green":
                            self.allBtn[i - 1][j]["bg"] = "red"
                        self.allBtn[i - 1][j]["state"] = "disabled"
                resultLabel = Label(self.root, text="You lose!", bg='gainsboro')
                resultLabel.grid(columnspan=self.buttonInColumns)
                return
            amount = howManyMines(numRow, numCol + 1, self.minesWeeperField)
            if amount == 0:
                self.allBtn[numRow - 1][numCol].configure(text='     ')
                self.allBtn[numRow - 1][numCol]["bg"] = "gainsboro"
                howManyZero(numRow, numCol + 1, self.minesWeeperField, self.allBtn, self.origColor, self.root)
                self.countClick = 0
                for i in range(0, self.buttonInRows):
                    for j in range(self.buttonInColumns):
                        if self.allBtn[i][j]["bg"] != self.origColor:
                            self.countClick += 1
                return
            self.allBtn[numRow - 1][numCol].configure(text=f"{amount}")
            self.allBtn[numRow - 1][numCol]["fg"] = f"{whatIsColor(amount, self.origColor)}"
            self.allBtn[numRow - 1][numCol]["bg"] = "gainsboro"
            self.countClick += 1
            self.isWinning()

    def newGame(self):
        self.minesWeeperField = createField(self.buttonInRows, self.buttonInColumns, self.minesInFiled)
        for i in range(1, self.buttonInRows + 1):
            allBtnInRow = []
            for j in range(self.buttonInColumns):
                allBtnInRow.append(Button(self.root, text='     ',
                                          command=lambda row=i, col=j: self.identifyButton(row, col)))
                allBtnInRow[-1].bind('<Button-3>', lambda event, row=i, col=j: self.rightButton(row, col))
                allBtnInRow[-1].grid(row=i, column=j, sticky="nsew")
            self.allBtn.append(allBtnInRow)

    def refreshOrExitFrame(self, goToMenu=0):
        if goToMenu:
            clearGameWindow(self.root, self.allBtn, self.minesWeeperField, 1)
            self.createMenuFrame()
        else:
            clearGameWindow(self.root, self.allBtn, self.minesWeeperField)
            self.amountMinesLabel.configure(text=f'{self.minesInFiled}')
            self.minesInFiledCopy = self.minesInFiled
            self.newGame()

    def createGameWindow(self, *args):
        clearMenuWindow(self.root)
        self.root.title(args[0])
        if args[0] == 'Beginner':
            self.buttonInRows = 9
            self.buttonInColumns = 9
            self.minesInFiled = 10
        elif args[0] == 'Intermediate':
            self.buttonInRows = 16
            self.buttonInColumns = 16
            self.minesInFiled = 40
        elif args[0] == 'Expert':
            self.buttonInRows = 16
            self.buttonInColumns = 30
            self.minesInFiled = 99
        elif args[0] == 'Custom':
            if int(args[1].get()) > 4 and int(args[2].get()) > 4:
                self.buttonInRows = int(args[1].get())
                self.buttonInColumns = int(args[2].get())
                if int(args[3].get()) > int(args[1].get()) * int(args[2].get()):
                    self.minesInFiled = int(args[1].get()) * int(args[2].get()) - 1
            else:
                # Label(self.root, text='Invalid input (width & height min 4)', fg='red').grid(row=7, columnspan=3)
                messagebox.showerror('Invalid input', 'width & height min 4')
                self.root.destroy()
        self.minesInFiledCopy = self.minesInFiled

        Button(self.root, text='Menu',
               command=lambda: self.refreshOrExitFrame(1)).grid(row=0, columnspan=2, sticky="nsew", ipady=4)
        self.root.bind("<Escape>", lambda event: self.refreshOrExitFrame(1))
        Label(self.root, text='or ESC', bg='gainsboro').grid(row=0, column=2, columnspan=2)
        Button(self.root, text='NG', command=self.refreshOrExitFrame).grid(
            row=0, column=self.buttonInColumns // 2, sticky="nsew", ipady=4)
        self.amountMinesLabel = Label(self.root, text=str(self.minesInFiled), font='10')
        self.amountMinesLabel.grid(row=0, column=self.buttonInColumns - 2, sticky="nsew", columnspan=2, ipady=4)
        self.newGame()

    def createMenuFrame(self):
        self.root.title("Minesweeper")
        self.root.configure(background='gainsboro')
        Label(self.root, text='Minesweeper', bg='gainsboro', fg='red', font='Courier 28 bold').grid(row=0, column=0,
                                                                                                    columnspan=3,
                                                                                                    sticky="nsew",
                                                                                                    pady=32)
        self.beginnerButton = Button(self.root, text='Beginner', font='Courier 14',
                                     command=lambda: self.createGameWindow('Beginner'))
        self.beginnerButton.grid(row=1, column=0, columnspan=3, pady=4)
        self.origColor = self.beginnerButton.cget("background")
        Button(self.root, text='Intermediate', font='Courier 14',
               command=lambda: self.createGameWindow('Intermediate')).grid(row=2, column=0, columnspan=3, pady=4)
        Button(self.root, text='Expert', font='Courier 14',
               command=lambda: self.createGameWindow('Expert')).grid(row=3, column=0, columnspan=3, pady=4)
        customHeight = StringVar()
        customWidth = StringVar()
        customMines = StringVar()
        Button(self.root, text='Custom', font='Courier 14',
               command=lambda h=customHeight, w=customWidth, m=customMines:
               self.createGameWindow('Custom', h, w, m)).grid(row=4, column=0, columnspan=3, pady=4)
        textBox1 = Entry(self.root, width=5, textvariable=customHeight, justify='center')
        textBox2 = Entry(self.root, width=5, textvariable=customWidth, justify='center')
        textBox3 = Entry(self.root, width=5, textvariable=customMines, justify='center')
        textBox1.insert(END, '16')
        textBox2.insert(END, '30')
        textBox3.insert(END, '145')
        textBox1.grid(row=5, column=0, padx=4)
        textBox2.grid(row=5, column=1, padx=4)
        textBox3.grid(row=5, column=2, padx=4)
        Label(self.root, text='height', bg='gainsboro').grid(row=6, column=0)
        Label(self.root, text='width', bg='gainsboro').grid(row=6, column=1)
        Label(self.root, text='mines', bg='gainsboro').grid(row=6, column=2)
        self.root.bind("<Escape>", lambda event: self.root.destroy())
