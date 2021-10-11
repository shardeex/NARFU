# 3. Создать два списка целых чисел. Рассортировать каждый из них,
# использую алгоритм обмена. Из двух рассортированных списков путём
# их слияния получить новый рассортированный список, не используя
# третий раз алгоритм сортировки.

import random


len_a = len_b = 10

a = sorted(list([random.randint(1, 100) for i in range(len_a)]))
b = sorted(list([random.randint(1, 100) for i in range(len_b)]))
c = []

print(f'исходные списки: {a} {b}')
counter_a, counter_b = 0, 0

while counter_a < len_a and counter_b < len_b:
    if a[counter_a] < b[counter_b]:
        c.append(a[counter_a])
        counter_a += 1
    else:
        c.append(b[counter_b])
        counter_b += 1

    # print(counter_a, counter_b)

if counter_a < counter_b:
    c += a[counter_a:]
else:
    c += b[counter_b:]

print(f'общий список: {c}')