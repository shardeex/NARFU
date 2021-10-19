# Вариант 1

import random

seq = list([random.randint(0, 10) for i in range(8)])
print(seq)

def min_max_seq(seq):
    return min(seq), max(seq)

def min_max_args(*args):
    return min(args), max(args)

print(min_max_seq(seq))
print(min_max_args(*seq))