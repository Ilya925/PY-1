"""Кортежи (tuple)"""

""" Кортеж - упорядоченный набор неизменяемых объектов"""
from string import ascii_lowercase, ascii_uppercase, digits, ascii_letters

print(ascii_lowercase)
print(ascii_uppercase)
print(digits)
print(ascii_letters)
t  = 22
tp = (22, 33, 44)
print(id(tp[0]), id(t))
# tp[0] = 220  не работает
print(tp[1])  # получение значения по индексу
print(tp[:-1])  # срез с кортежа
print(tp[::-1])
print(type(tp))  # тип объекта
print(list(tp))
string = 'qwerty'
lst = list(string)
print(lst)
print(''.join(lst))
tps = tuple(string)
print(tps)
print(''.join(tps))

print(ord('A'))  # lat
print(ord('А'))  # рус
print(ord('\n'))
print(ord('\t'))
print(ord('\r'))
print(ord('2'))
print(chr(1049))


n, m, z = 7, 5, 8
print(type(n))
print(n)

PI = 3.1415926,
print(PI[0])
print(type(PI))

# name, first, *marks, predlast, last = 'Ivan', 4, 5, 3, 5 ,7
# print(name)
# print(first)
# print(*marks)
# print(predlast)
# print(last)

tp = ('login', 'password')
print(tp)
print(id(tp))
buff = list(tp)
print(buff)
buff[-1] = 'qwerty'
print(buff)
tp = tuple(buff)
print(id(tp))
print(tp)

# tp = (22, 33, 44, 22)
# print(tp)
# print(len(tp))
# print(tp.count(22))
# print(tp.index(22))
# print(tp[0] == tp[-1])
# print(tp[0] is tp[-1])
# print(id(tp[0]), id(tp[-1]))

