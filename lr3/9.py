# Выяснить, является ли заданное число n членом арифметической прогрессии,
# первый член которой равен f, а шаг — s (n, f, s вводятся с клавиатуры).

n, f, s = map(int, input('введите n, f и s через пробел: ').split())

print('является.') if (n-f)%s == 0 else print('не является.')