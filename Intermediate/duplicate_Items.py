#Display all duplicate items from a list
sample_list = [10, 20, 60, 30, 20, 40, 30, 60, 70, 80]

exist = {}
dup = []

for i in sample_list:
    if i not in exist:
        exist[i] = 1

    else:
        dup.append(i)
print(dup)
