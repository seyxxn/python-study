a, b, c = map(int, input().split())

if (b >= c):
    print(-1)
    exit()
else :
    print(int(a/(c-b)+1))