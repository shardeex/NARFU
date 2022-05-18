import random

import numpy


c = (4, 2)
d = (2, 5)

a = numpy.array([random.randint(1, 9) for _ in range(numpy.prod(c))])
b = numpy.array([random.randint(1, 9) for _ in range(numpy.prod(d))])

a = a.reshape(c)
b = b.reshape(d)

print(numpy.dot(a, b))
