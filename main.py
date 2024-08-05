from functions import *

window = Tk()
window.geometry("{}x{}".format(fieldSize*20+15, fieldSize*20+15))
flag = PhotoImage(file= "flag.png")
bomb = PhotoImage(file= "bomb.png")
buttons = [[Button(window, height=1, width=2) for j in range(fieldSize)] for i in range(fieldSize)]

planting()
generateField(window, buttons, flag, bomb)
window.mainloop()