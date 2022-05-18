import random

import numpy


d = (3, 3, 2)

a = numpy.array([random.randint(1, 9) for _ in range(numpy.prod(d))])
a = a.reshape(d)
print(a)
