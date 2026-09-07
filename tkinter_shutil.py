import shutil
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog as fd
import os
from datetime import datetime

# shutil.copytree(r"C:\Users\Windows\Desktop\Proba_shutil",
#                 r"C:\Users\Windows\Desktop\Proba_shut_copy")
# shutil.move(r"C:\Users\Windows\Desktop\Proba_shutil\shut1_move",
#             r"C:\Users\Windows\Desktop\Proba_shut_copy")

root = Tk()
root.withdraw()

dir_ = fd.askdirectory(title='Выбираем папку')
if dir_:
    for file in os.listdir(dir_):
        if file.lower().endswith(('.jpg', '.jpeg', '.png')):
            file_path = os.path.join(dir_, file)  # формирую маршрут
            last_time = os.path.getmtime(file_path)
            dt = datetime.fromtimestamp(last_time)
            dt = dt.strftime('%d.%m.%Y %X')
            print(f'{file} изменен {dt}')




root.mainloop()