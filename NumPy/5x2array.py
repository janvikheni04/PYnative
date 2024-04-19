#Create a 5X2 integer array from a range between 100 to 200 such that the difference between each element is 10
import numpy
print("creatin array-5X2 numpy.arange")
a1 = numpy.arange(100,200, 10)
a1 = a1.reshape(5,2)
print(a1)