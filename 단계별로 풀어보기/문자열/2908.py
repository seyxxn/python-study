a,b = map(list, input().split())

a.reverse()
b.reverse()

x = int(a[0])*100 + int(a[1])*10 + int(a[2])
y = int(b[0])*100 + int(b[1])*10 + int(b[2])

if ( x > y):
    print(x)
elif ( x < y):
    print(y)
