from time import strftime
from tkinter import *
from tkinter import messagebox
import pygame as pg


def tick():
    global time_run
    current_time = strftime('%H:%M:%S')
    current_time1 = strftime('%H:%M')
    current_time2 = strftime('%H')
    text.config(text=current_time)
    if (time_run == current_time or time_run == current_time1
            or time_run == current_time2):

        time_run = ''
        pg.mixer.music.play()
    text.after(1000, tick)


def on():
    global time_run
    time_run = entry.get().strip()
    messagebox.showinfo('Время установки будильника',
                        f'Будильник установлен на {time_run}')


def off():
    global time_run
    time_run = ''
    pg.mixer.music.stop()
    messagebox.showwarning('Предупреждение',
                           f'Будильник отключен!')


pg.mixer.init()
pg.mixer.music.load('music.mp3')
time_run = ''
root = Tk()
root.config(bg='black')
WIDTH = root.winfo_screenwidth()
HEIGHT = root.winfo_screenheight()
X = 400
Y = 250
root.geometry(f"{X}x{Y}+{WIDTH // 2 - X // 2}"
              f"+{HEIGHT // 2 - Y // 2 - 20}")
root.title('Будильник')

text = Label(root, text='00:00:00')
text.config(font=('Arial', 50), bg='black', fg='lime')
text.pack()
entry = Entry(root, font=('Arial', 20), width=10, justify=CENTER)
entry.pack(pady=10)
entry.focus_set()

btn = Button(text='Включить', width=10, font=('Arial', 10), command=on)
btn.pack(pady=5)
btn1 = Button(text='Выключить', width=10, font=('Arial', 10), command=off)
btn1.pack()
# text1 = Label(root, text='Введите значение 1: ')
# text1.pack()

tick()

root.mainloop()
