# file = open('text.txt', 'r', encoding='utf-8')
# # s = file.read()
# # print(s)
# # s = file.readline()
# # print(s)
# s = file.readlines()
# print(s)
# file.close()

# for i in open('text.txt', encoding='utf-8'):
#     print(i.strip())

with open('text.txt', encoding='utf-8') as file:
    ls = file.read().title().split()
print(ls)
# ls.sort()

with open('text1.txt', 'w', encoding='utf-8') as file:
    for k, i in enumerate(ls, 1):
        file.write(f'{k}. {i}\n')