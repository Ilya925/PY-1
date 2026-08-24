# def proba():
#     print('proba')
#     return 'function'
#
# n = proba()
# print(n)


def summator(x=10, y=50):  # summator - имя функции, x и y -параметры
    return x + y


# res = summator(100, 20)
# print(res)
# print(summator(50, 30))
# print(summator(90))  # позиционный аргумент
# print(summator(y=10))  # ключевой аргумент


def many_args(*args, **kwargs):
    print(args)
    print(kwargs)
    return sum(args)


# print(many_args(2, 4, 3, 4, y=20, x=34))
# print(many_args())
# print(many_args(44, 66, c=76))


# Область видимости переменных
# параметры функции и определенные в ней переменные
# называются локальными
def number(k, m):
    global n
    n += 1
    print('N =', n)
    return str(n) + m


n = 10
# print(number('Маша +', ' Саша'))
# print('N модуля =', n)


def is_even(num: int) -> bool:
    """Определение четности числа.
    True - четное
    False - нечетное."""
    return num % 2 == 0
    # if num % 2 == 0:
    #     return True
    # else:
    #     return False


# print(is_even(8))
# print(is_even.__doc__)
def choice_even(x, y):
    for i in range(x, y+1):
        if is_even(i):
            print(i, end=' ')


# choice_even(100, 140)
# def num2(n):
#     if n > 1:
#         num2(n-1)
#     print(n)
#
# def num1(n):
#     if n > 1:
#         num2(n-1)
#     print(n)

# def num(n):
#     if n > 1:
#         num(n-1)
#     print(n)
#
# num(14)
"""
3! = 1 * 2 * 3 = 3 * 2!
2! = 1 * 2      =2 * 1!
1! = 1
n! = n * (n-1)!
"""

def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)


# print(fact(6))

def name(nm):
    cnt = 0
    def surname(snm):
        nonlocal cnt
        cnt += 1
        print(cnt, nm, snm)
    return surname

cnt = 100
snm = name('Саша')
snm('Petrova')
snm('Sidorova')

snm = name('Mary')
snm('Petrova')
snm('Sidorova')
snm('Andreeva')

def power(n):
    return n ** 2

n = power(5)
print(n)
n = (lambda n: n ** 2)(5)

print(n)