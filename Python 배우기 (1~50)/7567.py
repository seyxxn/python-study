plates = input()
res = 10

for i in range(1,len(plates)):
    if plates[i] == plates[i-1]:
        res += 5
    elif plates[i] != plates[i-1]:
        res += 10

print(res)