n = int(input())
chang = 100
sang = 100

for i in range(n):
    c, s = map(int, input().split())
    if c < s :
        chang = chang - s
    elif c > s :
        sang = sang - c
    else :
        pass
    
print(chang)
print(sang)