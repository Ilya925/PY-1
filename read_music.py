from tkinter import *

# root = Tk()
# root.geometry("870x500")
#
# text = Text(root, width=70, height=20,font=("Courier New", 15))
# text.pack()
# for inf in open('music.csv'):
#     ls = inf.split(';')
#     text.insert(END, f'{ls[0]:10} - {ls[1]:21} - {ls[2]:9} - {ls[3]}')
#
# root.mainloop()
import requests
from bs4 import BeautifulSoup
from django.templatetags.i18n import language_name

url = "https://www.hse.ru/staff/allat"


def get_main(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    name = soup.find("h1", class_="person-caption").text
    position = soup.find("span", class_="person-appointment-title").text[:-2]

    language = soup.find('dt', class_='b').find_all("dd")
    # print(language)
    print(f'({name}, {position})')
    for l in language:
        print(l.text)


lst = ("https://www.hse.ru/staff/allat",
       "https://www.hse.ru/org/persons/135897",
       "https://www.hse.ru/org/persons/63890353"
       )
for i in lst:
    get_main(i)
# get_main("https://www.hse.ru/staff/allat")
# get_main("https://www.hse.ru/org/persons/135897")
# get_main("https://www.hse.ru/org/persons/63890353")
