import random

div_7 = lambda x: x % 7 == 0
seq = list([random.randint(0, 70) for i in range(20)])
print(seq)

print(list(filter(div_7, seq)))