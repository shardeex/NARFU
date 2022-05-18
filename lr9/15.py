import random

import numpy


d = (10, 10)

a = numpy.array([random.randint(1, 9) for _ in range(numpy.prod(d))])
a = a.reshape(d)

mx = a.max()
a = numpy.where(a == mx, -1, a)

print(a)
