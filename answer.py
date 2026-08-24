def main(expression):
    a = []
    b = []
    c = []
    temp = expression
    signs = ['x^2', 'x', '']
    step = 0
    for i in a, b, c:
        print(i)
        for j in temp:
            if j == '-' or j.isdigit():
                i.append(j)
            elif j == '+':
                continue
            else:
                z = ''.join(i)
                temp = temp.replace(z + signs[step], '')
                step += 1
                break
        print(i)
    print(type(i), i)
    print(a, b, c)
    a = int(''.join(a))
    b = int(''.join(b))
    c = int(''.join(c))
    print(diskr(a, b, c))


def diskr(a, b, c):
    d = b ** 2 - 4 * a * c
    print('Дискриминант равен:', d)

    if d > 0:
        x1 = round((-b + d ** 0.5) / (2 * a), 2)
        x2 = round((-b - d ** 0.5) / (2 * a), 2)
        return x1, x2
    elif d == 0:
        x = -b / (2 * a)
        return x
    else:
        print('Нет корней.')


if __name__ == '__main__':
    main('12x^2+4x-6=0')