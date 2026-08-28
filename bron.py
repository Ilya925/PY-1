from tkinter import *


def color_(i):
    if i <= 3:
        color = "red"
    elif 4 <= i <= 6:
        color = "blue"
    else:
        color = "yellow"
    return color

def handler(num):
    btns[num - 1].config(bg="lightgray")


def unbuzy(num, row):
    color = color_(row)
    btns[num - 1].config(bg=color)

root = Tk()
root.title("Бронирование")
root.geometry("800x410+100+100")
frame1 = Frame(root)
frame2 = Frame(root)
frame1.pack(pady=10)
frame2.pack()
screen = Label(frame1, text='ЭКРАН')
screen.pack()
canvas = Canvas(frame1, width=400, height=60)
canvas.pack()
canvas.create_line(50,10, 350, 10, width=8, fill="light blue")

canvas.create_line(60, 40, 140, 40, width=4, fill="red")
canvas.create_text(100, 30, text=1000 )
canvas.create_line(160, 40, 240, 40, width=4, fill="blue")
canvas.create_text(200, 30, text=1100 )
canvas.create_line(260, 40, 340, 40, width=4, fill="yellow")
canvas.create_text(300, 30, text=2000 )

# btn1 = Button(frame2)
# btn1.config(text=1,font='Arial 10', justify=CENTER,
#             width=2, bg="red" )
# btn1.grid(row=0, column=0)
# btn2 = Button(frame2)
# btn2.config(text=2,font='Arial 10', justify=CENTER,
#             width=2, bg="red" )
# btn2.grid(row=0, column=1)
rows = 10
columns = 18
btns = []
for i in range(rows):
    row = Label(frame2, text=f'Ряд № {i + 1}')
    row.grid(row=i, column=0)
    for j in range(columns):
        num = i * columns + j + 1
        # if i <= 3:
        #     color = "red"
        # elif 4 <= i <= 6:
        #     color = "blue"
        # else:
        #     color = "yellow"
        color = color_(i)
        btn = Button(frame2)
        btn.config(text=f'{j + 1}', font='Arial 10', justify=CENTER,
                                width=2, bg=color, command=lambda x=num: handler(x))
        btn.grid(row=i, column=j + 1)
        btn.bind("<Button-3>", lambda event, nm=num, r=i: unbuzy(nm, r))

        btns.append(btn)


root.mainloop()

