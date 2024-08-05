from tkinter import *
import random

fieldSize = 20
values = [[0 for i in range(fieldSize)] for j in range(fieldSize)]
found = [[0 for i in range(fieldSize)] for j in range(fieldSize)]
finished = 0
numberOfBombs = int(fieldSize*fieldSize/7)

def generateField(root, buttons, flag, bomb):
    for y in range(fieldSize):
        for x in range(fieldSize):
            button = buttons[y][x]
            button.config(command= lambda y = y, x = x: clickedButton(x,y, root, buttons, bomb))
            button.bind('<Button-3>', lambda event, button=button: rightClick(event, button, flag))
            button.place(x=5+x*20, y=5+y*20)

def rightClick(event, button, flag):
    button.config(image=flag, height=20, width=20)
    button.bind('<Button-3>', lambda event, button=button: rightClickAgain(event, button, flag))

def rightClickAgain(event, button, flag):
    button.config(image = '', height=1, width=2)
    button.bind('<Button-3>', lambda event, button=button: rightClick(event, button, flag))

def planting():
    for i in range(numberOfBombs):
        x = random.randrange(fieldSize)
        y = random.randrange(fieldSize)
        while (values[y][x] > 8):
            x = random.randrange(fieldSize)
            y = random.randrange(fieldSize)

        if x != fieldSize-1:
            values[y][x+1] += 1
            if y != fieldSize-1:
                values[y+1][x+1] += 1
            if y != 0:
                values[y-1][x+1] += 1
        if x != 0:
            values[y][x-1] += 1
            if y != fieldSize-1:
                values[y+1][x-1] += 1
            if y != 0:
                values[y-1][x-1] += 1
        if y != fieldSize-1:
            values[y+1][x] += 1
        if y != 0:
            values[y-1][x] += 1

        values[y][x] = 69
        found[y][x] = 1

def clickedButton(x, y, root, buttons, bomb):
    buttonValue = values[y][x]
    if buttonValue > 10:
        for i in range(fieldSize):
            for j in range(fieldSize):
                if values[j][i]>10:
                    Button.config(buttons[j][i], image=bomb, height=18, width=18)
        gameOverWindow = Toplevel(root)
        Label(gameOverWindow, text="Game over").pack()
        Button(gameOverWindow, text="Start again", command=lambda: [startAgain(buttons), gameOverWindow.destroy()]).pack()
        return 0
    if buttonValue < 10 and buttonValue != 0:
        Button.config(buttons[y][x], image='', height=1, width=2, text=buttonValue, background='white')
        buttons[y][x].unbind('<Button-3>')
        found[y][x] = 1
    if buttonValue == 0:
        Button.config(buttons[y][x], image='', height=1, width=2, background='white')
        buttons[y][x].unbind('<Button-3>')
        found[y][x] = 1
        showAroundZero(x,y, root, buttons, bomb)
    
    finished = 1
    for i in range(fieldSize):
        for j in range(fieldSize):
            if found[j][i] == 0:
                finished = 0
    if finished == 1:
        victory = Toplevel(root)
        Label(victory, text="Congrats, you finished the game ^^").pack()

def startAgain(buttons):
    for y in range(fieldSize):
        for x in range(fieldSize):
            Button.config(buttons[y][x], text='', image='', height=1, width=2, background='#f0f0f0')
            values[y][x] = 0
            found[y][x] = 0
    planting()

def showAroundZero(x, y, root, buttons, bomb):
    if x!= fieldSize-1 and values[y][x]==0:
        if found[y][x+1] == 0:
            clickedButton(x+1,y, root, buttons, bomb)
    if x!= 0 and values[y][x]==0:
        if found[y][x-1] == 0:
            clickedButton(x-1,y, root, buttons, bomb)
    if y!= fieldSize-1 and values[y][x]==0:
        if found[y+1][x] == 0:
            clickedButton(x,y+1, root, buttons, bomb)
    if y!= 0 and values[y][x]==0:
        if found[y-1][x] == 0:
            clickedButton(x,y-1, root, buttons, bomb)

    if x!= fieldSize-1 and y != fieldSize-1 and values[y][x]==0:
        if found[y+1][x+1] == 0:
            clickedButton(x+1,y+1, root, buttons, bomb)
    if x!= fieldSize-1 and y != 0 and values[y][x]==0:
        if found[y-1][x+1] == 0:
            clickedButton(x+1,y-1, root, buttons, bomb)
    if x!= 0 and y != 0 and values[y][x]==0:
        if found[y-1][x-1] == 0:
            clickedButton(x-1,y-1, root, buttons, bomb)
    if x!= 0 and y != fieldSize-1 and values[y][x]==0:
        if found[y+1][x-1] == 0:
            clickedButton(x-1,y+1, root, buttons, bomb)