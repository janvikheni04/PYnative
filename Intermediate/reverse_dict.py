#Reverse Dictionary mapping\

dict1 = {'A': 65, 'B': 66, 'C': 67, 'D': 68}
dict2 = {i: key for key, i in dict1.items()}
print(dict2)
