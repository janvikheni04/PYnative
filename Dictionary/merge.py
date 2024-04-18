#Using a loop and update() method of a dictionary
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

a = dict1.copy()
a.update(dict2)
print(a)