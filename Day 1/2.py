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

# print(l_column)

similarity_score = 0

for i in l_column:
    if i in r_column:
        similarity_score += (int(i) * r_column.count(i))
        
        # print(f"For {i} the amount of times it appears in the right column is {r_column.count(i)}")
print(similarity_score)