n = int(input())

score = list(input().split())
result = 0
suc = []

for i in score:
    if int(i) == 1:
        result += 1

for i in range(n-1):
    if int(score[i]) == 1 and int(score[i+1]) == 1 :
        plus += 1
    else :
        plus = 0
    suc.append(plus)

print(result+sum(suc))