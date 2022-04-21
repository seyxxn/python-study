x = int(input())
star = 1
space = x - 1

for i in range(x):
    print(" "*space, "*"*star, sep="")
    star += 1
    space -= 1