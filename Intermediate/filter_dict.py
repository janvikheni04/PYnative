#Filter dictionary to contain keys present in the given list

d1 = {'A': 65, 'B': 66, 'C': 67, 'D': 68, 'E': 69, 'F': 70}

# Filter dict using following keys
l1 = ['A', 'C', 'F']

new_d = {i: d1[i] for i in l1}
print(new_d)