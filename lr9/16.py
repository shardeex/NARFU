import numpy


a = numpy.random.random(5)
v = 0.5

print(a, round(a[(numpy.abs(a - v)).argmin()], 8), sep='\n')
