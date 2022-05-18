lst = list(input().split(','))
res = 0

for i in lst:
    if i.isnumeric():
        res += 1
print(res)