import json
#
#
# class Narod:
#     def __init__(self, surname, name, second_name , age, sex):
#         self.surname = surname
#         self.name = name
#         self.second_name = second_name
#         self.age = age
#         self.sex = sex
#
#     def __str__(self):
#         return (f'{self.surname} {self.name} {self.second_name}:'
#                 f' {self.age} - {self.sex} ')
#
# l_narod = []
# d ={}
# for i in open('text.txt'):
#     ls = i.strip().split(',')
#     l_narod.append(Narod(ls[0], ls[1], ls[2], ls[3], ls[4]))
#     d[ls[0]] = ls[1:]
# for i in l_narod:
#     print(i, i.name)
# print(d)
# with open('text.json', 'w', encoding='utf-8') as f:
#     json.dump(d, f)

with open('text.json', encoding='utf-8') as f:
    d = json.load(f)

print(d)