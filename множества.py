"""Множества (set)"""

""" множество - набор неупорядоченных уникальных 
значений(неизменяемых объектов)"""

ls = [22, 33, 44, 44]
# st = {22, 33, 44, 44}
st = set()
st = set(ls)
# print(st)
# st.clear()
# print(st)
# st.add(100)
# st.update({'old', 32})
# print(st)
# n = st.pop()
# st.remove('old')
# st.discard(1001)
#
# print(st)
# print(n)
#
# try:
#     st.remove('old')
#     n = int(input('> '))
#     if n == 100:
#         raise TypeError(' Ошибка типа данных')
# except ValueError :
#     print('ввод символьного значения')
# except KeyError as err:
#     print('Ошибка по ключу', err)
# except Exception as err:
#     print(err)
# else:
#     print('Ok')
# finally:
#     print('всегда')

st1 = {1, 2, 33}
st2 = {1, 2, 44}

# res = st1.union(st2)  # Объединение множеств
res = st1 | st2

res = st1.intersection(st2)  # Пересечение множеств
res = st1 & st2

res = st1.difference(st2)  # вычитание множеств
res = st1 - st2

res = st1.symmetric_difference(st2) # симметрическая разность
res = st1 ^ st2

print(res)

st1 = {1, 2, 33}
st2 = {1, 2, 44}
st3 = {1, 2}

print(st3.issubset(st1))
print(st1.issuperset(st3))