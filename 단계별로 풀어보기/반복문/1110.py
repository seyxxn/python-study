count = 1
numFirst = int(input())

num = numFirst

while True:
    x = num % 10
    y = num // 10 + x
    num = x * 10 + (y % 10)
    if num == numFirst:
        break
    else :
        count += 1
    
print(count)