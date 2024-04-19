#Create a 4X2 integer array and Prints its attributes
import numpy
fa = numpy.empty([4,3], dtype = numpy.uint16) 
print("Print array:")
print(fa)

print("Shape is:", fa.shape)
print("Dimenstions are:", fa.ndim)
print("length of:", fa.itemsize)
