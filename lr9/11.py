import random

import numpy


d = (10, 10)

a = numpy.array([random.randint(1, 9) for _ in range(numpy.prod(d))])
a = a.reshape(d)

a = numpy.where(numpy.logical_and(a > 4, a < 7), a * -1, a)

print(a)
