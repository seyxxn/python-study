num = int(input())
total = 0
score = []

for x in range(num):
    test = input().split('X')
    total = 0
    for i in test:
        if (i=="") :
            continue
        else :
            for i in range(1, len(i)+1):
                total += i
    score.append(total)

print(*score, sep="\n")
