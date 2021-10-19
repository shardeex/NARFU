import random

div_7 = lambda n: n / 7

seq = list([random.randint(0, 70) for i in range(8)])
print(seq)

print(list(map(div_7, seq)))