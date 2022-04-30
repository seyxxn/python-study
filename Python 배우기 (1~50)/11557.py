t = int(input())
for i in range(t):
    n = int(input())
    uniAlcohol = {}
    for j in range(n):
        uniName, alcohol = map(str, input().split())
        uniAlcohol[uniName] = int(alcohol)

    maxAlcohol = max(uniAlcohol, key=uniAlcohol.get)

    print(maxAlcohol)