# Из не рассортированного списка целых чисел удалить повторяющиеся
# числа, оставив их по одному разу.

import random


numbers = list([random.randint(1, 9) for i in range(100)])

unique_numbers = []
for i in numbers:
    if i not in unique_numbers:
        unique_numbers.append(i)

print(unique_numbers)