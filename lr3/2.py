# Напечатать таблицу умножения на число n (значение n вводится с клавиатуры; 1≤n≤
# 9).

n = int(input('введите число: '))

for i in range(1, 10):
    print(f'{n}×{i} = {n*i}')