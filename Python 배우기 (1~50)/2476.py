n = int(input())
result = []

for i in range(n):
    res = 0
    a,b,c = map(int, input().split())
    if (a==b and b==c):
        res = 10000 + a * 1000
    elif (a==b and b != c):
        res = 1000 + a * 100
    elif (a==c and b != c):
        res = 1000 + a * 100
    elif (b==c and a != c):
        res = 1000 + b * 100
    else :
        res = max(a,b,c) * 100
    result.append(res)
    
print(max(result))