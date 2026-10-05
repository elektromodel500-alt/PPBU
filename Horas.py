from asyncio import current_task
from msvcrt import CRT_ASSEMBLY_VERSION
from tkinter import *
from tkinter import messagebox
import time
import pygame




def tick():
    global time_atarm
    current_time = time.strftime('%H:%M:%S')
    if (time_atarm == current_time or
            time_atarm == time.strftime('%H:%M') or
            time_atarm == time.strftime('%H')):
        time_atarm = ''
        pass
    screen_time.after(1000, tick)
    screen_time.config(text=current_time)


def on_click():
    global time_atarm
    time_atarm = entry_time.get()

    mb.showinfo('Включить будитьник')




def off_click():
    global time_atarm
    time_atarm = ''
    pass
    mb.showwarning ('Выключение будильника')




root = Tk()
root.title('Будильник')
root.config(background='black')
WIDTH = root.winfo_screenwidth()
HEIGHT = root.winfo_screenheight()
X = 400
Y = 210
root.geometry(f'{X}x{Y}+{WIDTH // 2 - X // 2}+'
              f'{HEIGHT // 2 - X // 2 - 25}')
screen_time = Label(root, text='00:00:00', font=('Arial', 50))
screen_time.config(font=('Arial', 50))
screen_time.pack()

entry_time = Entry(root, width=10, font=('Arial', 50))
entry_time.pack()

on = Button(root, text='Включить', font=('Arial', 10), command=on_click)
on.pack(pady=10)

off = Button(root, text='Выключить', font=('Arial', 10), command=off_click)
off.pack(pady=10)

tick()

root.mainloop()