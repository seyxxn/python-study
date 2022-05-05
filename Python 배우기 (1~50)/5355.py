t = int(input())

for i in range(t):
    word = []
    word = input().split()
    num = float(word[0])

    for i in range(1,len(word)):
        if word[i] == '@':
            num *= 3
        elif word[i] == '%':
            num += 5
        elif word[i] == '#':
            num -= 7
    print("{:.2f}".format(num))