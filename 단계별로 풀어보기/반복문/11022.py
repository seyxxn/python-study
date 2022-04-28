t = int(input())
res = []
first = []
second = []

for i in range(t):
    a,b = map(int, input().split())
    first.append(a)
    second.append(b)
    res.append(a+b)

for i in range(t):
    print("Case #%d: %d + %d = %d" %(i+1,first[i],second[i],res[i]))