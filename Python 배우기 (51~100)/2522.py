n = int(input())
m = 1

for i in range(1,n):
    print(" "*(n-i-1), "*"*(i))

print("*"*n)

for i in range(1,n):
    print(" "*(i-1), "*"*(n-i))


