"""СПИСКИ (list)
тип данных - списки, структура данных - массив."""
import random
from copy import deepcopy
# import copy

# print(__doc__)
"""Список - упорядоченный набор объектов"""
"""      0   1   2   3   4   """
nums = [22, 33, 44, 55, 99]
"""     -5  -4  -3  -2  -1   """
# print(nums[-3])
# print(nums[2])
# print(nums[-3:0:-1])
# print(nums[2:-5:-1])
# print(nums[2::-1])
#
# print(nums[2:])
# print(nums[::-1])  # реверсивный вывод информации
# nums = [20, 30, [40, 50]]
# s = nums
# s = nums.copy()
# s = nums[:]
# s = deepcopy(nums)
# s = copy.deepcopy(nums)
# nums[0] = 200
# nums[-1][0] = 400
# print(nums)
# print(id(nums))
# print(id(s))
# print(s)
# nums[:3] = 10, 20, 30
# print(nums)

# ls = [10, 'Dasha', 5.45, True, [67,'Andre']]
# lst = [['Masha', 18], ['Dasha', 22]]
# name = ['Masha', 'Dasha']
# age = [18, 22]
# print(name[1], age[1])
#
# nums = [55, 33, 44, 99, 77]
# print(id(nums))
# nums.append(100)  # временная сложность O(1) - константная
# nums.insert(3, 200)  # временная сложность O(n) - линейная
# nums.extend([1, 2])
# # nums += [1, 2]
# # nums = nums + [1, 2]
#
# nums.pop()  # удаляет последний элемент списка временная сложность O(1) - константная
# n = nums.pop()
# # del n
# nn = nums.pop(3)
# # while 55 in nums:
# #     nums.remove(55)
# nums.remove(100)
# print(nums.index(55))
# print(nums.count(55))
# print(sum(nums))
# print(max(nums))
# print(min(nums))
# nums.reverse()
# nums.sort(reverse=True)
#
# print(id(nums))
# print(nums)
# # print('n ==', n, 'nn ==', nn)
# print(len(nums))
#
# nums = []
# n = 0
# while  n != -273:
#     n = float(input('> '))
#     nums.append(n)
# nums.pop()

# print(f'min = {min(nums)}\nmax = {max(nums)}\nmean = {sum(nums)/len(nums):.2f}')
# print(nums)
#
nums = [22, 33, 44, 55, 99]
ls = [2, 3, 4, 5, 9, 10]
# # итерация по индексам
#
# for i in range(len(nums)): # 0 1 2 3 4
#     print(i, nums[i],  end='    ')
# print()
# # итерация по значениям
# cnt = 0
# for i in nums:
#     print(cnt, i, end='    ')
#     cnt += 1
# print()
# print(list(enumerate(nums)))
# for i in enumerate(nums):
#     print(i[0], i[1], end='    ')
# print()
# for i, j in enumerate(nums):
#     print(i, j, end='    ' )
# print()
names = ['Fedor', 'Alisa', 'Sasha', 'Glasha', 'Masha']
# names.sort()
# for n, name in enumerate(names, 1):
#     print(f'{n}. {name}')
#
# for i, j in zip(nums, ls):
#     print(i - j)

# генерация случайных вещественных чисел
# print(random.random())
# print(random.uniform(0.9, 1))
# print(random.uniform(-100, -99))
#
# # генерация целых случайных чисел
# print(random.randint(9, 10))
# print(random.randrange(2, 100, 2))
# print(random.randrange(1, 20, 2))
#
# # случайный выбор из коллекци
# print(random.choice(nums))
# print(random.choice(range(1, 10, 3)))
# print(random.choice(names))
#
# # генерация коллекции случайных объектов
#
# print(random.choices('абвгдеёжз', k=4))
# print(random.choices(names, k=7))
# print(random.sample(names, len(names)))
# print(random.sample(names, 4))

a = 'I like python, it is very useful for data analysis'
b = 'python is the best tool for dealing with big data'
# выписать вторую строку без слов в первой строке


a = a.replace(',', '')
a = a.split()
b = b.split()

c = []
for word in b:
    if word not in a:
        c.append(word)
# res = [word for word in b if word not in a]
# print(' '.join(c))
# print(' '.join([word for word in b if word not in a]))

# res = random.sample(range(1000000), 1000000)
# res.insert(0, 0)
# for n, i in enumerate(res, 1):
#     print(n, i)
#     if i == 0:
#         break

""" Ввести оценки каждого студента за семестр по 
одной дисциплине в формате
name 4 3 4 5 4 3 4 .
В консоль вывести ведомость имя ср.балл 
отсортированную по имени и 
вторую отсортрированную по среднему баллу.
"""
# n = int(input('введите кол-во студентов: '))
# data = {}
# for i in range(n):
#     name, *marks = input('формат: name 4 3 4 5 4 3 4: ').split()
#     print(marks)
#     marks = [int(mark) for mark in marks]
#     print(marks)
#     mean = sum(marks) / len(marks)
#     data[name] = round(mean, 2)
# print(data)

s ='rewiuyitqgeoiuytqewqyuttytqwerwqerwquytyutuyterwerutweurwqer'
# print({symb: s.count(symb) for symb in set(s)})
res = {}
cnt = 0
# for symb in set(s):
for symb in s:
    res[symb] = s.count(symb)
    cnt += 1
print(res)
print(cnt)