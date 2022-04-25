numList = [int(i) for i in range(1,10001)]

def plusNum(x):
    result = 0
    if len(str(x)) == 1:
        result = x + int(str(x)[0])
        return result
    elif len(str(x)) == 2:
        result = x + int(str(x)[0]) + int(str(x)[1])
        return result
    elif len(str(x)) == 3:
        result = x + int(str(x)[0]) + int(str(x)[1]) + int(str(x)[2])
        return result
    elif len(str(x)) == 4:
        result = x + int(str(x)[0]) + int(str(x)[1]) + int(str(x)[2]) + int(str(x)[3])
        return result
    elif len(str(x)) == 5:
        result = x + int(str(x)[0]) + int(str(x)[1]) + int(str(x)[2]) + int(str(x)[3]) + int(str(x)[4])
        return result

def isNotSelfNum(x):
    if len(str(x)) == 1:
        for y in range(1,x):
            if (plusNum(y) == x):
                return True
    elif len(str(x)) == 2:
        for y in range(1,x):
            if (plusNum(y) == x):
                return True
    elif len(str(x)) == 3:
        for y in range(1,x):
            if (plusNum(y) == x):
                return True
    elif len(str(x)) == 4:
        for y in range(1,x):
            if (plusNum(y) == x):
                return True
    elif len(str(x)) == 5:
        for y in range(1,x):
            if (plusNum(y) == x):
                return True

for x in numList:
    if isNotSelfNum(x):
        pass
    else:
        print(x)