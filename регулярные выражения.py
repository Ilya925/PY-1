import re

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

r+ - одно или более повторений r
r* - ноль или более повторений r
r? - ноль или одно повторение r
{n} - ровно n повторений
{n, m} - от n до m повторений
{n,} - от n и более повторений
{,m} - до m повторений 

"""
s = 'Annot#ation '
# print(re.findall(r'n?', s))
# print(re.findall(r'^.+#', s))
#
# pattern = re.compile(r'^.+#')
# print(pattern.findall(s))
# pattern = re.compile(r'\S+$')
# print(pattern.findall(s))

s = 'Победителем конкурса стал Иванов И.И.'
pattern = re.compile(r'\w+\s[А-Яа-яё]{1}\.[А-Яа-яё]{1}\.')
print(pattern.findall(s))

from string import ascii_letters, digits
import random


def generate_password(m):
    box = list(set(ascii_letters + digits) - {'1', 'I', 'l', 'O', 'o', '0'})
    # print(''.join(box))
    box1 = re.findall(r'[^Oo01Il]', ascii_letters + digits)
    # print(''.join(box1))

    # password = random.sample(box1, m)
    # pos = random.sample(range(m), 3)
    #
    # password[pos[0]] = password[pos[0]].lower() if password[pos[1]].isalpha() else 'n'
    # password[pos[1]] = password[pos[1]].upper() if password[pos[1]].isalpha() else 'J'
    # password[pos[2]] = str(random.randint(2, 9))
    #
    # return ''.join(password)
    password = ''
    while (not re.search(r'[A-Z]', password) or not re.search(r'[a-z]', password)
           or not re.search(r'[2-9]', password)):
        password = ''.join(random.sample(box1, m))
    return password


def main(n, m):
    passwords = set()
    while len(passwords) < n:
        passwords.add(generate_password(m))
    for password in passwords:
        print(password)


# main(20, 15)


# pattern = r'^\+\d-\d{3}-\d{3}-\d{2}-\d{2}$'
# pattern = r'^\d{11}$'
pattern = r'^79\d{9}$'
number = '+7-978-908-12-34'
number = number.replace('-', '').replace('+', '')
print(re.findall(pattern, number))
