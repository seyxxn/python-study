def selfNum():
    numList = list(range(1,10001)) # 1-10000 리스트 생성
    notSelfNumList = [] # self
    for x in numList :
        for i in str(x):
            x += int(i)
        if x <= 10000:
            notSelfNumList.append(x)
    for y in set(notSelfNumList):
        numList.remove(y)
    for z in numList:
        print(z)

selfNum()