import random

import numpy


d = (5, 5)

a = numpy.array([random.randint(1, 9) for _ in range(numpy.prod(d))], dtype=int)
a = a.reshape(d)

avg = round(a.mean())

print(a, avg, numpy.where(True, a - avg, None), sep='\n')
