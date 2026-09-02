import tkinter as tk


def show_event_info(event):
    info = f"""
    Виджет: {event.widget}\n
    Координаты: ({event.x},{event.y})\n
    Kоординаты экрана (x_root, y_root): {event.x_root}, {event.y_root}\n
    """
    if hasattr(event, 'char'):  # для клавиатуры
        info += f'Символ: {event.char}\n'
        info += f'Имя клавиши: {event.keysym}\n'
        info += f'Код клавиши: {event.keycode}\n'

    if hasattr(event, 'num'):
        info += f'Номер кнопки: {event.num}'

    print(info)


root = tk.Tk()
root.geometry("300x150+200+200")
frame = tk.Frame(root, width=200, height=100, background="light gray")
frame.pack(pady=20, padx=20)

frame.bind('<Button>', show_event_info)
frame.bind('<Key>', show_event_info)
frame.focus_set()

root.mainloop()