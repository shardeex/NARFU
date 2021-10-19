# Вариант 1
import math

x, y = map(float, input('введите x и y через пробел: ').split())

print(f'z1 = sin(x+1) - y - 1,2\nz2 = 2x + cos(y) - 2\n\nx = {x}, y = {y}\nz1 = {math.sin(x+1) - y - 1,2}\nz2 = {2*x + math.cos(y) - 2}')
