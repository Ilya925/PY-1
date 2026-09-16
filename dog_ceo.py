from tkinter import *
from tkinter import messagebox, ttk, filedialog
from io import BytesIO

from PIL import Image, ImageTk
import requests


def prod():
    progress['value'] = 5
    progress.start(40)
    root.after(4500, show_image)


def get_dog_url():

    try:
        resp = requests.get('https://dog.ceo/api/breeds/image/random')
        resp.raise_for_status()
        data = resp.json()
        return data['message']

    except Exception as err:
        messagebox.showerror('Ошибка','Ошибка чтения API')
        return None


def show_image():

    image_url = get_dog_url()

    try:
        resp = requests.get(image_url, stream=True)
        resp.raise_for_status()
        image_data = BytesIO(resp.content)
        img = Image.open(image_data)
        img.thumbnail((300, 300))
        img = ImageTk.PhotoImage(img)
        label.config(image=img)
        label.image = img
    except requests.RequestException as err:
        messagebox.showerror('Ошибка',
                             'Ошибка загрузки изображения')
    progress.stop()

root = Tk()
root.title("Изображения собачек")
root.geometry("600x500")

label = ttk.Label(root,)
label.pack(pady=15)
btn = ttk.Button(root,text='Загрузить изображение',
                 command=prod)
btn.pack()

progress = ttk.Progressbar(root,)
progress.pack(pady=15)

text = Text(root, width=50, height=20)
text.pack()


root.mainloop()