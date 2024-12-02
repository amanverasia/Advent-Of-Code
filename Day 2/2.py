abc = [16, 19, 21, 24, 21]

window = 2

for i in range(len(abc)-1):
    sum = abs(abc[i] - abc[i+1])
    if not (sum>0 and sum <4):
        print("UnSafe?")
