"""Словари ( dict )"""

"""словарь - набор неупорядоченных пар (ключ: значение), 
в котором ключи уникальны"""

d = {}
d = {'Pb': 'свинец', 'Au': 'Золото'}
print(d['Au'])
print(d.get('Pb1', 'нужный объект'))
print(d)
d['Pb'] = 'Свинец'  # изменение значения по существующему ключу

d['Fe'] = 'Железо'  # добавляем новую пару
n = d.setdefault(2, 22)
# n = d.setdefault('Pb', 22)
print(n)
d.update({3: 33, 2: 222})
key = 'Pb'
print(d[key])
n = d.pop('Fe')
nn = d.popitem()
print(n, nn)
print(d)

print(list(d.keys()))
print(list(d))
print(list(d.values()))
print(list(d.items()))
for k in d:
    print(k)

for v in d.values():
    print(v)

for k, v in d.items():
    print(k, v)
l = [22, 33, 44]
dd = dict.fromkeys(l, 'my item')
print(dd)
dd = {i: i**2 for i in range(10, 20)}
print(dd)
ls = [('Pb1', 'Свинец1'), ('Au1', 'Золото1'), (21, 22)]
dd = dict(ls)
print(dd)