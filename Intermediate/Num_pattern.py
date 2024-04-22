#number pattern

row = 5
x = 0

for i in range(row, 0, -1):
    x += 1
    
    for j in range(1, i+1):
        print(x, end=" ")
    print("\r")