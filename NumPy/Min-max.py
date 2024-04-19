#Print max from axis 0 and min from axis 1 from the following 2-D array.

import numpy
s1 = numpy.array([[34,43,73],[82,22,12],[53,94,66]])
print("Original array is:", s1)

b = numpy.amin(s1, 1)
print("Min from axis 1 is:", b)

c = numpy.amax(s1, 0)
print("Max of axis 0 is:", c)