"""СТРОКИ начальный курс."""
# s = 'Здравствуйте, \'гости!\''
"""  0123456789 """
s = 'ЗдраВствуйте, гости!'

print(s[19])
print(s[:10])
print(s[4:])
print(s[4::-1])
print(s[::-1])
s1 = 'казак'
print(s1[:])
print(s1[::-1])
print(__doc__)
# for i in range(len(s)):
#     print(i, s[i],end='   ')
#
# print()
# for i in s:
#     print(i, end='  ')
# print()
# print(len(s))
# 101 = 1 * 2**2 + 2**0
#          4     +   1  = 5
if s1 == s1[::-1]:
    print("Yes")
else:
    print("No")
print(s[4:0:-1])


# s = '    ЗдраВствуйте, гости!!!     '
s = 'ЗдраВствуйте, гости!'
s1 ='   '
print(s1.isalpha())  # состоит ли строка из букв
print(s1.isdigit())  # состоит ли строка из цифр
print(s1.isalnum())  # состоит ли строка из цифр и/или букв
print(s1.isspace())  # состоит ли строка из пробелов
print(s.isupper())  # все ли в строке буквы прописные
print(s.islower())  # все ли в строке буквы строчные
print(s.startswith('ЗдраВ' ))  # начинается ли строка с подстроки в скобках
print('раВ' in s)  # входит ли подстрока в переменную S
print(s.endswith('!'))
s1 = s.lower()  # все буквы строчные
print(s, s1)
print(s.upper())  # все буквы прописные
# s = '\033[4mЗдраВствуйте, гости!\033[0m' # режим подчеркивания
print(s)
print(s.title())
print(s.capitalize())
print(s.center(40))
print(s.rjust(40))
print(s.ljust(40))
print(s.swapcase())
print(s.strip('! З'))
print(s.rstrip())
print(s.lstrip())
print(s.index('т',7, 11))
print(s.find('т',11, 20))
print(s.replace('т', 'Т', 2).replace(',','.'))
s = 'ЗдраВствуйте, гости!\n'
s = s.strip()
ls = s.split(', ')  # изменят строку на список слов по разделителю
print(ls)
print(', '.join(ls)) # собирает строковые объекты списка в строку

# s1 = 'aaa bbb ccc ddd eee fff '
# s2 = '111 222 333 444 555 '
# # 'aaa 111 bbb 222 ccc 333 ddd 444'
# res = ''
# for i in range(0, len(s2), 4):
#     res += s1[i:i + 4] + s2[i:i + 4]
# print(res)

s = '-3x^2+4x-6=0' # a=-3, b = 4, c = -6
# -x^2-x=0: a=-1, b=-1, c =0

s = 'Строка символов'
print(s[1::2])
res = []
for n, symb in enumerate(s):
    if n % 2 != 0:
        res.append(symb)
print(''.join(res))
print(''.join([symb for n, symb in enumerate(s) if n % 2 != 0]))
