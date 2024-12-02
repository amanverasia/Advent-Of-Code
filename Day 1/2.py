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

abc = []
for num in l_column:
    if(num in r_column):
        # print(f"This {num} is in the right column")
        abc.append(num)
# print(abc)
print(len(abc))
counts_main = 0

for i in abc:
    counts = 0
    for number in r_column:
        # print()
        if int(i) == int(number):
            counts = counts + 1
    counts_main = counts_main + (counts*int(i))

print(counts_main)


    