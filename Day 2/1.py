data = []
with open("Day 2/input.txt") as fh:
    lines = fh.readlines()
    for line in lines:
        data.append(line.rstrip("\n"))

master_data = []

for i in range(len(data)):
    temp = []
    for j in ((data[i].split(" "))):
        temp.append(int(j))
    master_data.append(temp)

print(len(master_data))

unsafe_counter = 0
for i, row in enumerate(master_data):
    original_row = row.copy()
    row.sort()
    if original_row == row or original_row == row[::-1]:
        for j in range(len(original_row)-1):
            # print(original_row[j], original_row[j+1])
            sum = abs(original_row[j] - original_row[j+1])
            if not (sum>0 and sum <4):
                unsafe_counter += 1
                break
                
    else:
        unsafe_counter += 1


print(len(master_data) - unsafe_counter)

