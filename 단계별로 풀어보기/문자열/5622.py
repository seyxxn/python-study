word = input()
time = 0

for i in word:
    if ('A' <= i <= 'C'):
        time += 3
    elif ( i <= 'F'):
        time += 4
    elif ( i <= 'I'):
        time += 5
    elif ( i <= 'L'):
        time += 6
    elif ( i <= 'O'):
        time += 7
    elif ( i <= 'S'):
        time += 8
    elif ( i <= 'V'):
        time += 9
    elif ( i <= 'Z'):
        time += 10
    else :
        time += 11

print(time)