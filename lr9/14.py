import random

import numpy


d = (2, 2)

a = numpy.array([random.randint(1, 2) for _ in range(numpy.prod(d))])
b = numpy.array([random.randint(1, 2) for _ in range(numpy.prod(d))])

a = a.reshape(d)
b = b.reshape(d)

print(a, b, numpy.array_equal(a, b), sep='\n')
