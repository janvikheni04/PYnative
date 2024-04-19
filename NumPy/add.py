#Create a result array by adding the following two NumPy arrays. Next, modify the result array by calculating the square of each element\
import numpy

a1 = numpy.array([[5, 6, 9], [21 ,18, 27]])
a2 = numpy.array([[15 ,33, 24], [4 ,7, 1]])

r = a1+ a2
print("Adding array-", r)

for num in numpy.nditer(r, op_flags = ['readwrite']):
   num[...] = num*num
print("\nResult array after calculating the square root of all elements\n")
print(r)