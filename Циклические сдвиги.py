"""левый циклический сдвиг"""
# l = [22, 33, 44, 55, 99]
# temp = l[0]
# n = len(l)
# for i in range(n - 1):
#     l[i] = l[i + 1]
# l[-1] = temp
# print(l)
# l = [22, 33, 44, 55, 99]
# for i in range(n - 1):
#     l[i], l[i + 1] = l[i + 1], l[i]
# print(l)
#
# x = 10
# y = 20
#
# z = x
# x = y
# y = z
# print(x, y)
# x, y = y, x
# print(x, y)
#
# правый циклический сдвиг
# l = [22, 33, 44, 55, 99]
# temp = l[-1]
# n = len(l)
# for i in range(n - 1, 0, -1):
#     l[i] = l[i - 1]
# l[0] = temp
# print(l)
l = [22, 33, 44, 55, 99]
n = len(l)
for i in range(n - 1, 0, -1):
    l[i], l[i - 1] = l[i - 1], l[i]
    pass
print(l)