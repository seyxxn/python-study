floor = 0
roomNum = 0
t = int(input())
for i in range(t):
    h,w,n = map(int, input().split())
    if (n%h == 0) :
        floor = h
        roomNum = n // h
    else :
        floor = n % h
        roomNum = n // h + 1

    if roomNum < 10 :
        print(floor,"0",roomNum,sep="")
    else :
        print(floor,roomNum,sep="")
