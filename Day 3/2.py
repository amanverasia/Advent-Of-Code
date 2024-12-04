import re
data = []
with open("Day 3/input.txt", "r") as fh:
    lines = fh.readlines()
    for line in lines:
        data.append(line.rstrip("\n"))

# final_data = [] 
# for i in data:
#     final_data.append(re.findall("mul\(\d{1,3},\d{1,3}\)",i))
#     break


# temp = data[5].split("don't()")

final_data = [] 
for z in data:
    temp = z.split("don't()")
    for i in range(1, len(temp)):
        
        if len(temp[i].split("do()")) > 1:
            output = ""
            print(len(temp[i].split("do()")))
            # print("this ran")
            for stuff in range(1, len(temp[i].split("do()"))):
                print("this runs")
                output += temp[i].split("do()")[stuff]
            final_data.append(re.findall("mul\(\d{1,3},\d{1,3}\)",output))
    final_data.append(re.findall("mul\(\d{1,3},\d{1,3}\)",temp[0]))
    


sum = 0
for j in final_data:
    for i in j:
        sum = sum + ((int(i.replace("mul(","").replace(")", "").split(",")[0]) * int(i.replace("mul(","").replace(")", "").split(",")[1])))
print(sum)

