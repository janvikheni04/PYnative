employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

a = dict.fromkeys(employees, defaults)
print(a)
print(a['Emma'])