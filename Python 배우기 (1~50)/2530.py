hour, min, sec = map(int, input().split())
time = int(input())

sec += time
min += sec //60
hour += min // 60

print(hour%24, min%60, sec%60)