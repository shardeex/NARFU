# Даны два множества чисел. Выведите третье, состоящее из элементов первого и
# элементов второго множества, которых нет в первом.

import random

a = set([random.randint(1, 10) for i in range(5)])
b = set([random.randint(1, 10) for i in range(5)])
c = a.union(b)

print(f'Исходные множества: {a} {b}')
print(f'Третье: {c}')