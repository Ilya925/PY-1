from tkinter import *


def validation_func():
    text = entry.get().strip()
    corr_text = ''.join(symbl for symbl in text if symbl in "0123456789-+")
    if corr_text != text:
        entry.delete(0, 'end')
        entry.insert(0, corr_text)



root = Tk()
root.title('Валидация')
root.geometry('500x300+300+200')

Label(root, text='введите номер тлф', font='Arial 20').pack()
entry = Entry(root, width=10, font='Arial 20', justify='center')
entry.pack(pady=10)
entry.bind('<KeyRelease>', lambda event: validation_func())

root.mainloop()


