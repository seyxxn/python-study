n = input()
result = 0

lst = list(input().split())

for i in lst:
    if str(i)[-1] == n:
        result += 1

print(result)