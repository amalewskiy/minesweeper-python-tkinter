from random import randint
from tkinter import Button, messagebox


def clearMenuWindow(root):
    for widget in root.winfo_children():
        widget.destroy()


def clearGameWindow(root, allBtn, minesWeeperField, goToMain=0):
    allBtn.clear()
    minesWeeperField.clear()
    if goToMain:
        for widget in root.winfo_children():
            widget.destroy()
    else:
        for widget in root.grid_slaves():
            if int(widget.grid_info()["row"]) > 0:
                widget.destroy()


def createField(btnRow, btnCol, mines):
    minesWeeperField = [[0 if 0 < j < btnCol + 1 else -1 for j in range(btnCol + 2)] for i in range(btnRow + 2)]
    minesWeeperField[0] = [-1 for i in range(len(minesWeeperField[0]))]
    minesWeeperField[btnRow + 1] = [-1 for _ in range(len(minesWeeperField[0]))]
    for mine in range(mines):
        randRow = randint(1, btnRow)
        randCol = randint(1, btnCol)
        while minesWeeperField[randRow][randCol] == 1:
            randRow = randint(1, btnRow)
            randCol = randint(1, btnCol)
        minesWeeperField[randRow][randCol] = 1
    return minesWeeperField


def howManyMines(i, j, minesWeeperField):
    mineCount = 0
    if minesWeeperField[i - 1][j - 1] == 1: mineCount += 1
    if minesWeeperField[i - 1][j] == 1: mineCount += 1
    if minesWeeperField[i - 1][j + 1] == 1: mineCount += 1
    if minesWeeperField[i][j - 1] == 1: mineCount += 1
    if minesWeeperField[i][j + 1] == 1: mineCount += 1
    if minesWeeperField[i + 1][j - 1] == 1: mineCount += 1
    if minesWeeperField[i + 1][j] == 1: mineCount += 1
    if minesWeeperField[i + 1][j + 1] == 1: mineCount += 1
    return mineCount


def whatIsColor(number, oC):
    switcher = {
        1: 'blue',
        2: 'green',
        3: 'red',
        4: 'blue4',
        5: 'red4',
        6: 'magenta4'
    }
    return switcher.get(number, oC)


def aroundZero(i, j, minesWeeperField, allBtn, origColor, root):
    neighborButtons = [[i - 1, j - 1], [i - 1, j], [i - 1, j + 1],
                       [i, j - 1], [i, j], [i, j + 1],
                       [i + 1, j - 1], [i + 1, j], [i + 1, j + 1]]
    for neighbor in neighborButtons:
        if minesWeeperField[neighbor[0]][neighbor[1] + 1] != -1 and \
                allBtn[neighbor[0] - 1][neighbor[1]]["bg"] == origColor:
            amount = howManyMines(neighbor[0], neighbor[1] + 1, minesWeeperField)
            if amount == 0:
                howManyZero(neighbor[0], neighbor[1] + 1, minesWeeperField, allBtn, origColor, root)
                txt = '     '
            else:
                txt = str(amount)
            allBtn[neighbor[0] - 1][neighbor[1]] = Button(root, text=txt, bg='gainsboro',
                                                          fg=f'{whatIsColor(amount, origColor)}')
            allBtn[neighbor[0] - 1][neighbor[1]].grid(row=neighbor[0], column=neighbor[1], sticky="nsew")


def howManyZero(i, j, minesWeeperField, allBtn, oC, root):
    if minesWeeperField[i][j] == -1:
        return
    if howManyMines(i, j, minesWeeperField) == 0:
        minesWeeperField[i][j] = -1
    aroundZero(i, j - 1, minesWeeperField, allBtn, oC, root)


def exitApplication(root):
    msgBox = messagebox.askquestion('Exit Application', 'Are you sure you want to exit the application?',
                                    icon='warning')
    if msgBox == 'yes':
        root.destroy()
