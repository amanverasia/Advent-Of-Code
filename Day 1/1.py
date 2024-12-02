data = []
with open("Day 1/input.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        data.append(line.rstrip("\n"))

l_column = []
r_column = []
for line in data:
    # print(line.split(" "))
    l_column.append(line.split(" ")[0])
    r_column.append(line.split(" ")[3])

l_column.sort()
r_column.sort()
sum = 0
for i in range(len(l_column)):
    sum += abs(int(l_column[i]) - int(r_column[i]))
    # print(l_column[i], r_column[i])
print(sum)