a, b, c = map(int, input().split())
x = 1

if (b >= c):
    print(-1)
    exit()
else :
    while(True):
        if(x> a/(c-b)):
            break
        else:
            x += 1
print(x)