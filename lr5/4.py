#  Вариант 1

import random

is_even = lambda n: not n % 2

a = list([random.randint(0, 10) for i in range(8)])
b = list([random.randint(0, 10) for i in range(8)])
print(a, b)

counter_a = 0
for i in a:
    counter_a = counter_a + 1 if is_even(i) else counter_a

counter_b = 0
for i in b:
    counter_b = counter_b + 1 if not is_even(i) else counter_b

print(counter_a, counter_b)