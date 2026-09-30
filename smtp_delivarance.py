import smtplib
from email.message import EmailMessage
from email.utils import parseaddr
from tkinter import *


def validate_email(email):
    try:
        name, addr = parseaddr(email)
        return '@' in addr and '.' in addr.split('@')[-1]
    except ValueError:
        return False


def save():
    with open('save.txt', 'w') as file:
        file.write(sender_email_entry.get() + '\n')
        file.write(recipient_email_entry.get() + '\n')
        file.write(password_entry.get() + '\n')


def load():
    try:
        with open('save.txt', 'r') as file:
            credentials = file.readlines()
            sender_email_entry.insert(0, credentials[0].strip())
            recipient_email_entry.insert(0, credentials[1].strip())
            password_entry.insert(0, credentials[2].strip())
    except FileNotFoundError:
        pass


def send_email():
    save()
    sender_email = sender_email_entry.get().strip()
    recipient_email = recipient_email_entry.get().strip()
    if not validate_email(sender_email) or not validate_email(recipient_email):
        result_label.config(text='Неверный формат Email ')
        return

    password = password_entry.get().strip()
    subject = subject_entry.get().strip()
    body = body_text.get('1.0', 'end')

    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = recipient_email

    server = None

    try:
        server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
        server.login(sender_email, password)
        server.send_message(msg)
        # print('Письмо от правлено')
        result_label['text'] = 'Письмо от правлено'
    except Exception as err:
        print(f'Ошибка:{err}')
    finally:
        if server:
            server.quit()



# sender_email = 'stigorleon65@yandex.ru'
# recipient_email = 'aligol6573@gmail.com'
# password= 'clezaeftjavmuhxd'
# subject = 'Прверка рассылки с программы'
# body = 'текст сообщения'

root = Tk()
root.title('Отправка Email')
root.geometry('500x300')

Label(text='Oтправитель (Email)').grid(row=0, column=0, sticky=W)
sender_email_entry = Entry(root)
sender_email_entry.grid(row=0, column=1)

Label(text='Получатель (Email)').grid(row=1, column=0, sticky=W)
recipient_email_entry = Entry(root)
recipient_email_entry.grid(row=1, column=1)

Label(text='Пароль приложения (Email)').grid(row=2, column=0, sticky=W)
password_entry = Entry(root)
password_entry.grid(row=2, column=1)

Label(text='Тема:').grid(row=3, column=0, sticky=W)
subject_entry = Entry(root)
subject_entry.grid(row=3, column=1)

Label(text='Текст сообщения:').grid(row=4, column=0, sticky=W)
body_text = Text(root,height=10,width=40)
body_text.grid(row=4, column=1)

(Button(text='Отправить', command=send_email).grid(row=5, column=1, sticky=E))
result_label = Label(text='')
result_label.grid(row=6, column=1, sticky=W)

load()

root.mainloop()
validate_email('stigorleon65@yandex.ru')