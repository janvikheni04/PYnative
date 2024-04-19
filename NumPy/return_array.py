#Following is the provided numPy array. Return array of items by taking the third column from all rows
import numpy
s1 = numpy.array([[11 ,22, 33], [44, 55, 66], [77, 88, 99]])
print("Array:", s1)

print("\n new array on third col. of all rows")
n1 = s1[...,2]
print(n1)

