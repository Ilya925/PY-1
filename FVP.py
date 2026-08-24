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
n = list(map(lambda n: n * 2, l))
print(n)