from tkinter import *
from tkinter import messagebox as mb
import time

import pygame
import pygame as pg

pg.mixer.init()
pg.mixer.music.load('music.mp3')


def tick():
    global time_alarm
    current_time = time.strftime("%H:%M:%S")
    if (time_alarm == current_time or
            time_alarm == time.strftime("%H:%M") or
            time_alarm == time.strftime("%H")):
        time_alarm = ''
        pg.mixer.music.play()
    screen_time.after(1000, tick)
    screen_time.config(text=current_time)


def on_click():
    global time_alarm
    time_alarm = entry_time.get().strip()

    mb.showinfo('Включение будильника',
                f'Будильник включен на {time_alarm}')


def off_click():
    global time_alarm
    time_alarm = ''
    entry_time.delete(0, END)
    pg.mixer.music.stop()
    mb.showwarning('Выключение будильника',
                f'Будильник выключен')
