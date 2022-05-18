import random

import numpy


d = (8, 8)

a = numpy.zeros(numpy.prod(d), dtype=int).reshape(d)
a[1::2, ::2] = a[::2, 1::2] = 1

print(a)
