from tkinter import *


def res(event=None):
    item = entry.get().strip()
    try:
        item = int(item) + 100
    except ValueError:
        item = 'Free'
    result.config(text=item)


root = Tk()
WIDTH = root.winfo_screenwidth()
HEIGHT = root.winfo_screenheight()
X = 400
Y = 250
root.geometry(f"{X}x{Y}+{WIDTH // 2 - X // 2}"
              f"+{HEIGHT // 2 - Y // 2 - 20}")
root.title('Проба')

text = Label(root, text='Введите значение: ')
text.config(font=('Arial', 20), bg='light gray')
text.pack()
entry = Entry(root, font=('Arial', 20), width=20, justify=CENTER)
entry.pack(pady=10)
entry.focus_set()
result = Label(root, text='   ' * 10, bg='light gray', font=('Arial', 20))
result.config(justify=CENTER)
result.pack()
btn = Button(text='Кнопка', command=res)
btn.pack(pady=10)
# text1 = Label(root, text='Введите значение 1: ')
# text1.pack()

entry.bind('<Return>', res)

root.mainloop()
