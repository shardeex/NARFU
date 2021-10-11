# 17. Дан список в формате [[1, 10], [2, 20], [3, 30]. [4, 40]]. Переписать его в виде
# [1, 10, 2, 20, 3, 30, 4, 40]. Использовать генератор.

import random


numbers = list([[random.randint(0, 100), random.randint(0, 100)] for i in range(random.randint(5, 10))])
print(f'исходный массив: {numbers}')

new_numbers = list([j for i in numbers for j in i])
print(f'новый массив: {new_numbers}')