import numpy
from matplotlib import pyplot
a=numpy.zeros([2,3])
print(a)
b=a
b[0,1]=1.5
b[1,0]=2
print(a)
print(b)

pyplot.imshow(a,interpolation="nearest")