n = int(input())
total = n * 2 - 1
for i in range(n):
    print(" "*(i), "*"*(total-2*i), sep="")