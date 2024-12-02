data = []
with open ("Day 1/number.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        data.append(line.split('\n')[0])

for line in data:
    print(line)