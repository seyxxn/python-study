word = input()

for i in range(len(word)):
    if i%10 == 9:
        print(word[i])
    else:
        print(word[i],end="")