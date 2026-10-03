import re
from re import findall

# s = 'Абревиатура'
#
# print(re.match(r'Аб', s))
# # if re.match(r'aб', s):
# #     print('Yes')
# # else:
# #     print('No')
#
# s = 'Annotation'
# res = re.search(r't', s)
# print(res)
#
# res = re.findall(r'n', s)
# print(res)
#
# res = re.finditer(r'n', s)
# print(list(res))

"""    Спецсимволы """

# \d - любая цифра
# \D - любое нечисловое значение
# \s - символы пробелов
# \S - все кроме символов пробелов
# \w - буква, цифра или нижнее подчеркивание
# \W - все кроме буквы, цифры или нижнего подчеркивания
# \bслово\b
"""
. - любой символ кроме переноса строки
^ - начало строки
$ - конец строки
[abc] - любой символ из скобок
[^abc] - любой символ кроме из скобок
a | b - символ a или b
[A-Za-z0-9]
КВАНТИФИКАТОРЫ

r+ - одно или более значений r
r* - ноль или более значений r
r? - ноль или одно значений r
{n} - ровно n значений
{n, m} - от n до m значений
{n,} - от n и более значений
{,m} - до m значений 

"""
# s = 'Annot#ation '
# print(re.findall(r'n?', s))
# print(re.findall(r'^.+#', s))
#
# pattern = re.compile(r'^.+#')
# print(pattern.findall(s))
# pattern = re.compile(r'\S+$')
# print(pattern.findall(s))

# s = 'Победителем конкурса стал Иванов И.И.'
# pattern = re.compile(r'\w+\s[А-Яа-яё]{1}\.[А-Яа-яё]{1}\.')
# print(pattern.findall(s))

from string import ascii_letters, digits
import random


# def generate_password(m):
#     box = list(set(ascii_letters + digits) - {'1', 'I', 'l', 'O', 'o', '0'})
    # print(''.join(box))
    # box1 = re.findall(r'[^Oo01Il]', ascii_letters + digits)
    # print(''.join(box1))

    # password = random.sample(box1, m)
    # pos = random.sample(range(m), 3)
    #
    # password[pos[0]] = password[pos[0]].lower() if password[pos[1]].isalpha() else 'n'
    # password[pos[1]] = password[pos[1]].upper() if password[pos[1]].isalpha() else 'J'
    # password[pos[2]] = str(random.randint(2, 9))
    #
    # return ''.join(password)
    # password = ''
    # while (not re.search(r'[A-Z]', password) or not re.search(r'[a-z]', password)
    #        or not re.search(r'[2-9]', password)):
    #     password = ''.join(random.sample(box1, m))
    # return password

#
# def main(n, m):
#     passwords = set()
#     while len(passwords) < n:
#         passwords.add(generate_password(m))
#     for password in passwords:
#         print(password)


# main(20, 15)


# pattern = r'^\+\d-\d{3}-\d{3}-\d{2}-\d{2}$'
# pattern = r'^\d{11}$'
# pattern = r'^79\d{9}$'
# number = '+7-978-908-12-34'
# number = number.replace('-', '').replace('+', '')
# print(re.findall(pattern, number))


"""

Задача 1. Проверка email-адреса
Условие:
Напишите функцию is_valid_email(email), которая проверяет, является ли строка корректным email-адресом.
Простая проверка: наличие @, домена и зоны (2+ символа).

Решение:"""

def is_valid_email(email: str) -> bool:
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+$'
    return bool(re.match(regex, email))

# Пример
print(is_valid_email("test@example.com"))  # True
print(is_valid_email("test@example"))      # False
print(is_valid_email("test.example.com"))  # False

"""
Задача 2. Извлечение дат из текста
Условие:
Дан текст. Найдите все даты в формате ДД.ММ.ГГГГ.
"""
text = "Сегодня 12.05.2023, а завтра 13.05.2023."
dates = re.findall(r'\b\d{2}\.\d{2}\.\d{4}\b', text)
print(dates)


"""
Задача 3. Замена повторяющихся пробелов
Условие:
Замените все последовательности пробелов (2 и более) на один пробел.
"""
text = "Это    текст   с   лишними пробелами."
print(text)
result = re.sub(r'\s{2,}', ' ', text)
print(result)

"""
Задача 4. Слова с заглавной буквы
Условие:
Найдите все слова, начинающиеся с заглавной буквы (русские и английские).

"""
text = "Москва и Санкт-Петербург — города России. London is the capital."
words = re.findall(r'\b[A-ZА-Я][а-яa-z]*\b', text)
print(words)
"""
Задача 5. Извлечение чисел (целых и дробных)
Условие:
Извлеките все числа из строки, включая дробные с точкой.
"""
text = "Цена 12.5 рублей, скидка 10%, итого 11.25."
numbers = re.findall(r'\d+(?:\.\d+)?', text)
print(numbers)
"""
Задача 6. Проверка сложности пароля
Условие:
Пароль должен содержать минимум 8 символов, 
хотя бы одну заглавную, одну строчную, одну цифру 
и один спецсимвол.
"""
def is_strong_password(password: str) -> bool:
    """Проверяет пароль на сложность."""
    if len(password) < 8:
        return False
    regex = [r'^[A-Z]',
             r'[a-z]',
             r'\d',
             r'[!@*#$%^&(),.?".{}:<>]'
             ]
    return all((re.search(r, password) for r in regex))


print('Strong', is_strong_password('Pass&word2'))
print(is_strong_password('Password2'))
print(is_strong_password('Pass&word'))
# print(re.search(r'[!@*#$%^&(),.?".{}:<>]', 'Password2'))
# result = any([True, False, False])
# result = all([True, True, True])
# print('result', result)
"""
Задача 7. Извлечение HTML-тегов
Условие:
Найдите все HTML-теги в строке и выведите их названия.
"""
html = '<div>Start <p>Programm</p> </div>'
tags = re.findall(r'</?(\w+)>', html)
print(tags)

"""
Задача 8. Именованные группы для разбора логов
Условие:
Дан лог: "2023-05-12 10:23:45 ERROR Сообщение об ошибке".
Извлеките дату, время, уровень и сообщение.
"""
log = "2023-05-12 10:23:45 ERROR Сообщение об ошибке"

regex = (r'(?P<date>\d{4}-\d{2}-\d{2}) (?P<time>\d{2}:\d{2}:\d{2}) '
         r'(?P<level>\w+) (?P<message>.*)')
print(re.findall(regex, log))
"""

Задача 9. Жадные и ленивые квантификаторы
Условие:
Извлеките текст между кавычками, используя ленивый квантификатор.


text = 'Он сказал: "Привет", а она ответила: "Пока".'
"""

text = 'Он сказал: "Привет", а она ответила: "Пока".'
quotes = re.findall(r'"(.*?)"', text)
print(quotes)
"""
Задача 10. Опережающая проверка (lookahead)
Условие:
Найдите все числа, после которых идёт слово «рублей».
"""
text = "1000 рублей, 200 долларов, 3000 рублей."
result = re.findall(r'\d+(?= рублей)', text)
print(result)
"""
Задача 11. Разделение строки с помощью re.split
Условие:
Разделите строку по запятым, точкам с запятой и пробелам, 
игнорируя пустые элементы.

"""
text = """apple, banana; cherry  date
qwerty;engine"""
result = re.split(r'[,\s;\n]+', text)
print(result)

"""
Задача 12. Флаги re.IGNORECASE и re.MULTILINE
Условие:
Найдите все строки, начинающиеся со слова «error»
 (без учёта регистра) в многострочном тексте.


"""
log = """Error: file not found
warning: low memory
ERROR: access denied
info: ok
"""

errors = re.findall(r'^error.*$', log, re.IGNORECASE | re.MULTILINE)
print(errors)


"""


 Извлечение HTML-тегов

html = '<a><b>'

# Жадный
print(re.findall(r'<.*>', html))   # ['<a><b>']

# Ленивый
print(re.findall(r'<.*?>', html))  # ['<a>', '<b>']
Пример 2. Текст в кавычках

text = 'Он сказал: "Привет", а она: "Пока".'

print(re.findall(r'".*"', text))   # ['"Привет", а она: "Пока"']
print(re.findall(r'".*?"', text))  # ['"Привет"', '"Пока"']

Пример 3. Цифры
s = '12345'

print(re.findall(r'\d+', s))   # ['12345']
print(re.findall(r'\d+?', s))  # ['1', '2', '3', '4', '5']
Ленивый \d+? каждый раз захватывает минимально возможное — одну цифру.

Пример 4. Диапазон {m,n}

s = '12345'

print(re.findall(r'\d{2,4}', s))   # ['1234']  (жадный взял 4 цифры)
print(re.findall(r'\d{2,4}?', s))  # ['12', '34'] (ленивый взял по 2)

Пример 5. Optional ? и ??

s = 'a'

print(re.findall(r'a?', s))   # ['a', '']  (сначала попытался взять 'a')
print(re.findall(r'a??', s))  # ['', '']  (сначала попытался взять пустоту)
Жадный a? предпочитает совпадение с a, ленивый a?? — пустую строку.

5. Почему это важно?
Жадные квантификаторы удобны, когда нужно захватить всё до последнего вхождения разделителя.
Ленивые — когда нужно остановиться на первом вхождении.
Неправильный выбор может привести к избыточному захвату или катастрофическому бэктрекингу.


6. Краткая памятка
Ситуация                    	Жадный	Ленивый
Взять всё до последнего >	     <.*>	<.*?>
Взять текст между кавычками	    ".*"	".*?"
Найти первое слово до пробела	\w+	    \w+? (редко нужно)
Разбить цифры по одной	        \d+	    \d+?
Запомните:

Жадный = «бери больше, потом отдай, если не сходится».
Ленивый = «бери меньше, потом добавь, если не сходится».
Оба варианта могут давать разные результаты, и выбор зависит от задачи.
"""