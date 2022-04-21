nowHour, nowMin = input().split(" ")
needTime = int(input())
needTimeHour = needTime // 60
needTimeMin = needTime % 60

finishHour = int(nowHour) + int(needTimeHour)
finishMin = int(nowMin) + int(needTimeMin)

if (finishMin >= 60):
    finishHour = finishHour + (finishMin // 60)
    finishMin = finishMin % 60

if (finishHour > 23):
    finishHour = finishHour-24
    
print(finishHour, finishMin)