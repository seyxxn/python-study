n = int(input())
score = list(map(int, input().split()))
maxScore = max(score)
global sum 
sum = 0 

for i in range(n):
    score[i] = score[i]/maxScore*100
    sum = sum + score[i]

print(sum/n)