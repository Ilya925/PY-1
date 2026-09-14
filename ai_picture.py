import tkinter as tk
from tkinter import messagebox, filedialog as fd
import asyncio
from io import BytesIO

from PIL import Image, ImageTk
import requests
from g4f.client import AsyncClient
from translate import Translator


async def gen_url(nm):
    client = AsyncClient()
    response = await client.images.generate(
        prompt=nm,
        model="flux-2-pro",
        response_format="url"
    )
    image_url = response.data[0].url
    print(f"Generated image URL: {image_url}")
    return image_url


def load_image(url):
    global img_s
    try:
        response = requests.get(url)
        response.raise_for_status()
        image_data = BytesIO(response.content)
        img_s = Image.open(image_data)
        img_s.thumbnail((600, 500), Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(img_s)
    except Exception as err:
        messagebox.showerror("Error", err)
        return None


def forward():
    nm = prompt.get().strip()
    nm = translate_ru_en.translate(nm.capitalize())
    url = asyncio.run(gen_url(nm))
    if url:
        img = load_image(url)
    if img:
        label.config(image=img)
        label.image = img


def save():
    global img_s
    if img_s is None:
        print('Нет изображения')
        return
    fp = fd.asksaveasfilename(
        defaultextension='.png',
        filetypes=[('PNG', '.png'), ('JPEG', '.jpg'), ('All_files', '*.*')],
        initialfile='picture'
    )
    if fp:
        img_s.save(fp)
        print(f'Изображение сохранено: {fp}')


translate_ru_en = Translator(from_lang='ru', to_lang='en')
img_s = None

root = tk.Tk()
root.title('Pictures')
root.geometry('600x600')

frame1 = tk.Frame(root)
frame1.pack(pady=10)
frame2 = tk.Frame(root)
frame2.pack()

prompt = tk.Entry(frame1, width=50, font='Arial 12')
prompt.grid(row=0, columnspan=2, pady=5)
prompt.insert(0, 'Kittens')
forw = tk.Button(frame1, text='Next', command=forward, font='Arial 12')
forw.grid(row=1, column=0)
forw = tk.Button(frame1, text='Save', command=save, font='Arial 12')
forw.grid(row=1, column=1)

label = tk.Label(frame2)
label.pack()

forward()

root.mainloop()
