from os import remove
num = int(input())
avgs = []

for x in range(num):
    score = []
    score = input().split(' ')
    score = list(map(int, score))
    student = score[0]
    del score[0]

    avg = sum(score) / student

    score = list(filter(lambda x : x > avg , score))

    overAvg = ( len(score) / student ) * 100

    avgs.append(overAvg)

for i in avgs:
    print(f'{i:.3f}%')
