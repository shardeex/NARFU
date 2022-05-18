import random

import numpy


d = (10)

a = numpy.array([random.randint(1, 9) for _ in range(numpy.prod(d))])
a = a.reshape(d)

a.sort()

print(a)
