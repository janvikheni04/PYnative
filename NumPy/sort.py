#Sort following NumPy array
#Case 1: Sort array by the second row
#Case 2: Sort the array by the second column

import numpy

s1 = numpy.array([[34,43,73],[82,22,12],[53,94,66]])
print("Original array is:", s1)

sortrow = s1[:, s1[1,:].argsort()]
print("Sorted array by second row is:", sortrow)

sortcol = s1[s1[:, 1].argsort()]
print("Sort array by second col:", sortcol)