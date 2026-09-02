from typing import Union, Optional, List, Dict


class Person:
    def __init__(self, name, age):
        self.__name: str = name
        self.__age: int = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    def __str__(self):
        return f'{self.__name} - {self.__age}'


class Flat:
    """Класс описывающий квартиру."""
    def __init__(self, number):
        self.__number: int = number
        self.__persons: List[Person] = []

    @property
    def number(self):
        return self.__number

    @property
    def persons(self):
        return self.__persons

    def add_person(self, *persons: Person) -> None:
        for person in persons:
            if not isinstance(person, Person):
                raise TypeError('Объект не является экземпляром класса "Persone"')
            self.__persons.append(person)

    def display(self):
        max_name = max(self.__persons, key=lambda x: len(x.name))
        mx = len(max_name.name)
        print(self)
        for i, person in enumerate(self.__persons, 1):
            print(f'\t\t\t{i}. {person.name:{mx}} - {person.age}')

    def __str__(self):
        return (f'\t\tКвартира: №{self.__number} ')


class Floor:
    def __init__(self, numb):
        self.__numb: int = numb
        self.__flats: List[Flat] = []


p1 = Person('John Lenon', 33)
p2 = Person('Pol Mackartney', 43)
p3 = Person('Klava Koka', 30)
p4 = Person('Said Abdurahman ibn Hattab', 80)
p5 = Person('Ny', 12)

kv45 = Flat(45)
kv46 = Flat(46)
kv45.add_person(p1, p2)
kv46.add_person(p3, p4, p5)
kv45.display()
kv46.display()
# print(Flat.__doc__)

