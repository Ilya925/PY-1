"""while"""
import math

# i = 0
# while i < 10:
#     i += 1
#     if i == 7:
#         continue  # прерывает итерацию
#     print(i,  end=' ')

# i = 0
# while i < 10:
#     i += 1
#     if i == 17:
#         break  # прерывает цикл
#     print(i,  end=' ')
# else:
#     print('\nDone')
# print('\nEND')

# symbols = input('> ').upper()
# while symbols != 'END':
#     print(symbols, end=' ')
#     symbols = input('>> ').upper()

# n = int(input('> '))
# sm = 0
# cnt = 0
# while n != 0:
#     sm += n
#     cnt += 1
#     n = int(input('>> '))
# print('Средняя температура за период: "', round(sm / cnt, 2), '"', sep='')
# print(f'Средняя температура за период: {sm / cnt:.2f}')

"""
35 100
71 cm
"""
# n = 71
# n1 = 33
# n2 =42
# print(n1, n2,'\n' + str(n), 'sm')
# print(f'{n1} {n2}\n{n} sm')

""" sm = 3 + 2 +  1
123 % 10 = 3
    //10 = 12  % 10 = 2
               //10 = 1 % 10 = 1 
                        //10 = 0
"""
#
# n = int(input('> '))
# nn = n
# sm = 0
# cnt = 0
# while n > 0:
#     remince = n % 10  # получаем последнюю цифру числа
#     sm += remince  # прибавляем полученную цифру в sm
#     cnt += 1  # увеличиваем счетчик на единицу
#     n //= 10  # получаем целую часть числа после отделения последней цифры
# print(f'В числе "{nn}" {cnt} ц. суммой {sm}.')

# n = int(input('> '))  # 123
# res = 0
# while n > 0:
#     remince = n % 10  # 3 -> 2 -> 1
#     res = res * 10 + remince  # 3 -> 30 + 2= 32 -> 320 + 1 = 321
#     n //= 10  # 12 -> 1 -> 0
# print(res)

""" НОД
36  24 -> 36 - 24 = 12
12  24 -> 24 - 12 = 12
12  12 -> 12 = 12 ->nod

"""
# n1 = int(input('> '))
# n2 = int(input('>> '))
# print(f'NOD = {math.gcd(n1, n2)}')
# while n1 != n2:
#     if n1 > n2:
#         n1 -= n2  # n1 = n1 - n2
#     else:
#         n2 -= n1
# print(f'NOD = {n1}')

# for n in range(100, 200):
#     for i in range(2, n):
#         if n % i == 0:
#             break
#     else:
#         print(n, end=' ')
#
# while True:
#     n = input('> ')
#     n1 = input('>> ')
#     if n.isnumeric() and n1.isnumeric():
#         n = int(n)
#         n1 = int(n1)
#     res = n + n1
#     print(f'{'Cлово получилось: ' if isinstance(res, str) else "Сумма равна"} {res}')
#     if res == 'stop':
#         break
while True:
    time = ('Mожет быть временем суток '
            if 0<= (n := int(input('> ')))<=24 else
            'Не может быть временем суток ')
    print(time)
    if n < 0:
        break
print(__doc__)