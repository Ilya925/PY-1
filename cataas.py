import os.path
from tkinter import *
from tkinter import filedialog as fd

from PIL import Image, ImageTk
import requests
from io import BytesIO


def load_image(url):
    global img_s
    try:
        resp = requests.get(url)
        resp.raise_for_status()
        image_data = BytesIO(resp.content)
        img_s = Image.open(image_data)
        img_s.thumbnail((600, 450), Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(img_s)
    except Exception as err:
        print(f'Ошибка {err}')
        return None


def set_image():
    img = load_image(url)
    if img:
        label.config(image=img)
        label.image = img


def exit():
    root.destroy()


def save_picture():
    global img_s
    if img_s is None:
        print('Нет изображения')
        return
    # def_name = os.path.basename(name_file)
    fp = fd.asksaveasfilename(
        defaultextension='.png',
        filetypes=[('PNG', '.png'), ('JPEG', '.jpg'), ('All_files', '*.*')],
        initialfile='picture'
    )
    if fp:
        img_s.save(fp)
        print('Save OK')


img_s = None
root = Tk()
root.title('Cats')
root.geometry('600x500+20+100')
label = Label()
label.pack()
# btn = Button(text='Следующая', command=set_image)
# btn.pack(pady=10)
menu_bar = Menu(root)
root.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='Next', command=set_image)
file_menu.add_separator()
file_menu.add_separator()
file_menu.add_command(label='Save', command=save_picture)
file_menu.add_separator()
file_menu.add_command(label='Exit', command=exit)

# url='https://cataas.com/cat'
url = 'https://cataas.com/cat/cute'
set_image()
root.mainloop()
