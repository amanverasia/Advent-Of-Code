data = []
with open("Day 1/input.txt") as f:
    lines = f.readlines()
    for line in lines:
        data.append(line.rstrip("\n"))

l_column = []
r_column = []
for i in data:   
    l_column.append(i.split(" ")[0])
    r_column.append(i.split(" ")[3])

l_column.sort()
r_column.sort()

sum = 0
for i in range(len(l_column)):
    sum = sum + abs(int(l_column[i]) - int(r_column[i]))
print(sum) # 3714264
3714264