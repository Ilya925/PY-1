from functools import reduce

l = [22, 33, 44]

# n = map(str, l)
# print(next(n))
# print(next(n))
# print(next(n))
# n1 = [str(i) for i in l]
# print(n, n1)

# def power(n):
#     return n * 2

# n = list(map(power, l))
l = [22, 33, 44]
l1 = [2, 3, 44]
# n = list(map(lambda n: n * 2, l))
# n = list(map(lambda n, m: n - m, l, l1))
n = list(map(lambda n, m: n > m, l, l1))

n = list(filter(lambda x: x % 2 == 0, l))
nn = [i for i in l if i % 2 == 0]
print(n)
print(nn)
nn = []
for i in l:
    if i == 10:
        nn.append(i)
        break

city = ['У', 'ф', 'а', '-', 4, 5]
# city = map(str, city)
# res = ''.join(city)
l = [1, 2, 3, 4, 5]
res = reduce(lambda n, m: str(n) + str(m), city)
# res = reduce(lambda n, m: n * m, l)
print(res)

def concat(n, m):
    print('N =', n)
    print('M =', m)
    print( str(n) + str(m))
    return str(n) + str(m)


res = reduce(concat, city)