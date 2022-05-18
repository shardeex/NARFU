import random

import numpy


d = (random.randint(3, 9), random.randint(3, 9))

a = numpy.ones(numpy.prod(d), dtype=int).reshape(d)
a[1: -1, 1: -1] = 0

print(a)
