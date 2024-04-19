#Delete the second column from a given array and insert the following new column in its place.
import numpy as np

sampleArray = np.array([[34,43,73],[82,22,12],[53,94,66]]) 

print("Delete second col;")
sampleArray = np.delete(sampleArray, 1, axis=1)
print(sampleArray)

newColumn = np.array([[10,10,10]])
print("Array after inserting")
sampleArray = np.insert(sampleArray, 1, newColumn, axis=1)
print(sampleArray)