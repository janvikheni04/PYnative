with open('Intermediate/sample.txt', 'r') as file:
    f = file.read().replace('\n', ' ')
    print(f)