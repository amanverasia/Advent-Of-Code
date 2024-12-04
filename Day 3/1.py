import re
data = []
with open("Day 3/input.txt", "r") as fh:
    lines = fh.readlines()
    for line in lines:
        data.append(line.rstrip("\n"))

final_data = [] 
for i in data:
    final_data.append(re.findall("mul\(\d{1,3},\d{1,3}\)",i))

sum = 0
for j in final_data:
    for i in j:
        sum = sum + ((int(i.replace("mul(","").replace(")", "").split(",")[0]) * int(i.replace("mul(","").replace(")", "").split(",")[1])))
print(sum)
# # for j in final_data:
#     for i in j:
        

# print(sum)