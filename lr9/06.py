import random

import numpy


d = (12, 12)

a = numpy.array([random.randint(1, 99) for _ in range(numpy.prod(d))])
mx, mn = max(a), min(a)  # secret way
a = a.reshape(d)
mx, mn = a.max(), a.min()  # normal way (max & min won't work in this array)
print(a, mx, mn, sep='\n')
