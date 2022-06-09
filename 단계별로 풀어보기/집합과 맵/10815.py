n = int(input())
cardNum =set(map(int, input().split()))

m = int(input())
checkNum = list(map(int, input().split()))

for i in range(len(checkNum)):
    if checkNum[i] in cardNum:
        checkNum[i] = 1
    else :
        checkNum[i] = 0

print(*checkNum)
