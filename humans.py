"""Напишите класс Human (Человек). Экземпляр класса инициализируется
 с аргументами: имя, произвольное количество сущностей,
 именованный аргумент – уровень магии со значением по умолчанию 0.

Класс обеспечивает выполнение методов (hm – экземпляр класса):

hm.change_name() – изменить имя – к имени через пробел добавляется
строка-аргумент;
экземпляру класса можно прибавить строку: hm += line – строка
дописывается к списку сущностей, уровень магии увеличивается на
 длину строки, нацело деленную на 4;
экземпляры класса можно вычитать друг из друга: hm2 = hm - hm1 –
возвращается новый экземпляр класса с атрибутами – имя составленное
 из первых трёх букв первого и последних трёх второго, обе части с
 большой буквы, сущности только те, что есть у первого, но нет у второго,
 порядок алфавитный, уровень магии по умолчанию;
экземпляр класса можно вызвать с аргументом-числом: возвращается
список из указанного числа сущностей с начала;
экземпляры класса можно сравнивать: сначала по уровню магии,
затем по количеству сущностей, затем по имени по алфавиту;
для печати возвращается строка вида: Human by name <name>
(<entities>, <magic>) Человек по имени <имя> (<сущности через запятую и пробел>, <уровень магии>)
Пример:
Ввод
hm = Human('Illmarrannen', 'Forgiving', 'Forgiven', magic=2)
hm.change_name('Rual')
id_hm = id(hm)
hm += 'Skyman'
print(hm, hm(2), sep='\n')
print(id_hm == id(hm))
Вывод:
Human by name Illmarrannen Rual (Forgiving, Forgiven, Skyman, 3)
['Forgiving', 'Forgiven']
True

Bвод:     hm = Human('Marran', 'Hanger', 'Stick', 'Wizzard', magic=10)
hm1 = Human('Lart', 'Wizzard')
print(hm, hm1, sep='\n')
print(hm > hm1, hm <= hm1, hm == hm1)
hm2 = hm - hm1
print(hm2)
print(hm2 > hm1, hm2 <= hm, hm2 != hm)

Вывод:
Human by name Marran (Hanger, Stick, Wizzard, 10)
Human by name Lart (Wizzard, 0)
True False False
Human by name MarArt (Hanger, Stick, 0)
True True True
"""


class Human:
    def __init__(self, name, *essence, magic=0):
        self.name = name
        self.magic = magic
        self.essence = list(essence)

    def change_name(self, name):
        self.name += ' ' + name

    def __add__(self, line):
        self.essence.append(line)
        self.magic += len(line) // 4
        return self

    def __call__(self, num):
        return self.essence[:num]

    def __sub__(self, other):
        name = self.name[:3] + other.name[-3:].capitalize()
        essence = list(set(self.essence) - set(other.essence))
        essence.sort()

        return Human(name, *essence, magic=0)

    def __eq__(self, other):
        if self.magic == other.magic:
            if len(self.essence) == len(other.essence):
                if self.name == other.name:
                    return True
        return False

    def __gt__(self, other):
        if self.magic > other.magic:
            return True
        elif self.magic == other.magic and len(self.essence) > len(other.essence):
            return True
        elif self.name > other.name and len(self.essence) == len(other.essence):
            return True
        return False

    def __lt__(self, other):
        if self.magic < other.magic:
            return True
        elif self.magic == other.magic and len(self.essence) < len(other.essence):
            return True
        elif self.name < other.name and len(self.essence) == len(other.essence):
            return True
        return False

    def __le__(self, other):
        if self.magic <= other.magic:
            return True
        else:
            return False

    def __ne__(self, other):
        if (self.magic != other.magic or len(self.essence) != len(other.essence)
                or self.name != other.name):
            return True
        return False

    def __str__(self):
        return f'Человек по имени {self.name} ({", ".join(self.essence)}, {self.magic})'


hm = Human('Marran', 'Hanger', 'Stick', 'Wizzard', magic=10)
hm1 = Human('Lart', 'Wizzard')
print(hm, hm1, sep='\n')
print(hm > hm1, hm <= hm1, hm == hm1)
hm2 = hm - hm1
print(hm2)
print(hm2 > hm1, hm2 <= hm, hm2 != hm)
