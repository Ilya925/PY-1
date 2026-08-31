from typing import Tuple
import matplotlib.pyplot as plt
# name=['Masha', 'Alex', 'Dasha']
# age = [20, 30, 40]
# for i,(j, k) in enumerate(zip(name, age), 1):
#     print(f'{i}. {j} - {k}')

# people = [('Masha', 20), ('Alex', 30), ('Dasha', 40)]
# d_people = dict(people)
# print(d_people)
# people = {'Masha': {'age': 20, 'sex': 'female'},
#           'Alex': {'age': 30, 'sex': 'male'},
#           'Dasha': {'age': 40, 'sex': 'female'}
#           }

# def sm(v1: Tuple[int, int], v2: tuple):
#     x = v1[0] + v2[0]
#     y = v1[1] + v2[1]
#     return x, y
#
#
# v1 = (17, 12)
# v2 = (5, 8)
# v = sm(v1, v2)
# print(v)

class Vector(object):
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Vector(x, y)

    def display_add(self, other):
        res = self + other
        x1 = [0, self.x]
        y1 = [0, self.y]
        x2 = [0, other.x]
        y2 = [0, other.y]
        rx = [0, res.x]
        ry = [0, res.y]

        plt.plot(x1, y1, x2, y2, rx, ry, '-.g')
        plt.show()


    def __str__(self) -> str:
        return f'Vector({self.x}, {self.y})'



v1 = Vector(10, 17)
v2 = Vector(9, 4)
v3 = Vector(50, 50)
# v1.display_add(v2)
v = v1 + v2 + v3
print(v)