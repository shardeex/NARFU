# Последовательность Фибоначчи образуется так: первый и второй члены
# последовательности равны 1, каждый следующий равен сумме двух предыдущих (1,
# 1, 2, 3, 5, 8, 13, ...). Найти первое число в последовательности Фибоначчи, большее n
# (значение n вводится с клавиатуры; n > 1).

n = int(input('введите число: '))
a = 0
b = 1

for i in range(2, n):
    a, b = b, a + b
    if b > n:
        print(b)
        break