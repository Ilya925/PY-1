from turtle import *

from prompt_toolkit.key_binding.bindings.named_commands import backward_word

# import turtle as t
colormode(255)  # разрешаем использовать режим RGB
shape('turtle')
color((117, 2, 84), (238, 242, 22))  # определение цвета пера и заполнения
pensize(4)  # ширина пера
speed(.9)  # cкорость пера (0-1)

# begin_fill()  # начало заполнения фигуры
# for _ in range(2):
#     fd(100)  #   движение вперёд на 100 пикселей (forward)
#     lt(90)  # изменение угла движения влево на 90 град.
# end_fill()  # завершение заполнения
# fillcolor('#16F21A')  # только цвет заполнения
# begin_fill()
# for _ in range(3):
#     fd(100)
#     lt(120)
# end_fill()
# fillcolor((238, 242, 22))
# fd(100)
# backward(100)  # движение назад без смены направления
# penup()  # поднять перо
# goto(-100, 100)  # перейти в координату
# pendown()  # опустить перо
# r = 191
# g = 33
# b = 142
# step = 0
# for i in range(200, 10, -20):
#     fillcolor(r, g, b)
#     for _ in range(6):
#         begin_fill()
#         for _ in range(3):
#             fd(i)
#             lt(120)
#         # circle(i)
#         end_fill()
#         rt(60)
#     r += 7
#     g += 6
#     b += 5
#
#     # penup()
#     # step -= 150
#     # goto(step, 0)
#     pendown()
# penup()
# goto(0, 0)
# pendown()

# for lng in range(200, 100, -20):
#
#     for _ in range(3): # 0 1 2
#         fd(lng)
#         rt(120)
#     penup()
#     backward(200)
#     pendown()

tr = Turtle('turtle')
tr.color('green', 'yellow')

tr1 = Turtle('turtle')
tr1.color('red', 'yellow')
tr2 = Turtle('turtle')
tr2.color('blue', 'yellow')
tr.goto(100, 0)
tr2.goto(-100, 0)
tr1.lt(90)
tr1.fd(100)
lt(90)
tr2.lt(180)


mainloop()
