# from importlib.metadata import entry_points
from tkinter import *


def answer(event):
    answ = num.get().strip()
    result.configure(text=answ)


root = Tk()
root.title('Hola')
WIDHT = root.winfo_screenwidth()
HEIGHT = root.winfo_screenheight()

X = 300
Y = 100
print(WIDHT, HEIGHT)
root.geometry(f'{X}x{Y}+{WIDHT // 2 - X // 2}+'
              f'{HEIGHT // 2 - X // 2 - 25}')

promt = Label(text='Введите значение', font=('Arial', 20))
promt.pack()

#promt.pack(side=BOTTOM)

num = Entry(width=5, font='Arial 12', justify='center')
num.pack()
result = Label(text='', font='Arial 12')
result.pack(pady=10)
num.bind('<Return>', answer)

root.mainloop()
