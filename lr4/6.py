# Дан список целых чисел. Напечатать:
# а) все чётные элементы
# б) все элементы, оканчивающиеся нулём

import random

numbers = [random.randint(1, 100) for _ in range(20)]
print('# numbers:', *numbers)

# a)
print('# even:', *[n for n in numbers if n % 2 == 0])

# б)
print('# divisible by 10:', *[n for n in numbers if n % 10 == 0])