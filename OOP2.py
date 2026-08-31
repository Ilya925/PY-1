class People:
    def __init__(self, name, age, sex='female'):
        self.__name = name
        self.__age = age
        self.__sex = sex

    # def get_name(self):
    #     return self.__name
    #
    # def set_name(self, name):
    #     self.__name = name
    #
    # name = property(get_name, set_name)
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value

    @property
    def sex(self):
        return self.__sex

    def __str__(self):
        return f'{self.__name} - {self.__age} years old {self.__sex}'


class Student(People):
    vuzs = {'MГУ': 5,
            'ЯВВФУ': 4,
            'MГПУ': 4
            }
    def __init__(self, name, age, vuz, rang, sex='female'):
        super().__init__(name, age, sex)
        self.__vuz = vuz
        self.__rang = rang if 0 < rang <Student.vuzs[self.__vuz] else None

    @property
    def vuz(self):
        return self.__vuz

    @vuz.setter
    def vuz(self, value):
        if not isinstance(value, str):
            raise TypeError('Тип данных должен быть строкой')
        self.__vuz = value

    @property
    def rang(self):
        return self.__rang

    @rang.setter
    def rang(self, value):
        if not isinstance(value, int):
            raise TypeError('Тип данных должен быть целым числом')
        if  value < 1 or value > Student.vuzs[self.__vuz]:
            raise ValueError('Значение вне диапазона')
        self.__rang = value


    def __str__(self):
        return (f'{self.name} - {self.age} years old\n '
                f'{self.sex} {self.__vuz}:{self.__rang} курс')


if __name__ == '__main__':
    p1 = People('John', 18, 'male')
    p2 = People('Mary', 19)

    print(p2)
    print(p1)
    # print(p1.get_name())
    # p1.set_name('Joline')
    print(p1)
    print(p1.name)
    p1.name = 'John'
    print(p1)
    std1 = Student('Alex', 19, 'MГУ', 1, 'male')
    std2 = Student('Glasha', 19, 'MГПУ', 6)
    print(std1)
    print(isinstance(std1, People))
    print(isinstance(std1, Student))
    print(std1.vuzs)
    print(std2.vuzs)
    print(Student.vuzs)
    print(std2)
    std2.rang=6
    print(std2)