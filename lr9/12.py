import random

import numpy


d = (6, 6)

a = numpy.array([[i for i in range(d[0])] for _ in range(d[1])])
a = a.reshape(d)

print(a)
