from random import randint
from tkinter import Button, messagebox


def clearMenuWindow(root):
    """This function clear all elements on "MenuWindow"."""
    for widget in root.winfo_children():
        widget.destroy()


def clearGameWindow(root, allBtn, minesWeeperField, goToMain=0):
    """This function clear all elements on "GameWindow"."""
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
    """This function return new field with size: param1 & param2 and amount mines: param3."""
    minesWeeperField = [[0 if 0 < j < btnCol + 1 else -1 for j in range(btnCol + 2)] for _ in range(btnRow + 2)]
    minesWeeperField[0] = [-1 for _ in range(len(minesWeeperField[0]))]
    minesWeeperField[btnRow + 1] = [-1 for _ in range(len(minesWeeperField[0]))]
    for mine in range(mines):
        randRow = randint(1, btnRow)
        randCol = randint(1, btnCol)
        while minesWeeperField[randRow][randCol] == 1:
            randRow = randint(1, btnRow)
            randCol = randint(1, btnCol)
        minesWeeperField[randRow][randCol] = 1
    return minesWeeperField


def howManyMines(i, j, minesweeperField):
    """This function return amount mines near clicked button."""
    mineCount = 0
    if minesweeperField[i - 1][j - 1] == 1: mineCount += 1
    if minesweeperField[i - 1][j] == 1: mineCount += 1
    if minesweeperField[i - 1][j + 1] == 1: mineCount += 1
    if minesweeperField[i][j - 1] == 1: mineCount += 1
    if minesweeperField[i][j + 1] == 1: mineCount += 1
    if minesweeperField[i + 1][j - 1] == 1: mineCount += 1
    if minesweeperField[i + 1][j] == 1: mineCount += 1
    if minesweeperField[i + 1][j + 1] == 1: mineCount += 1
    return mineCount


def whatIsColor(number, originalColor):
    """This function return color for font button depending on the number (param1) of mines near it."""
    switcher = {
        1: 'blue',
        2: 'green',
        3: 'red',
        4: 'blue4',
        5: 'red4',
        6: 'cyan4',
        7: 'gray1'
    }
    return switcher.get(number, originalColor)


def aroundCell(i, j, minesWeeperField, allBtn, origColor, root):
    """Read doc about "howManyZero".
    This function called "howManyZero" when all neighbor cells don't have mines.
    If neighbor cells has at least one mine, function change button."""
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
            allBtn[neighbor[0] - 1][neighbor[1]] = Button(root, text=txt, bg='light gray',
                                                          fg=f'{whatIsColor(amount, origColor)}')
            allBtn[neighbor[0] - 1][neighbor[1]].grid(row=neighbor[0], column=neighbor[1], sticky="nsew")


def howManyZero(i, j, minesWeeperField, allBtn, originalColor, root):
    """This recursion function which works together with function "aroundZero".
    This function called "aroundZero" when the cell has not been checked."""
    if minesWeeperField[i][j] == -1:
        return
    if howManyMines(i, j, minesWeeperField) == 0:
        minesWeeperField[i][j] = -1
    aroundCell(i, j - 1, minesWeeperField, allBtn, originalColor, root)


def exitApplication(root):
    """This function called when user pushed Esc on Menu window, and called messagebox with question."""
    msgBox = messagebox.askquestion('Exit Application', 'Are you sure you want to exit?',
                                    icon='warning')
    if msgBox == 'yes':
        root.destroy()
