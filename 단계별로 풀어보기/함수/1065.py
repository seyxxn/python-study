n = int(input())

list = [int(i) for i in range(1,n+1)]

def hansu(list):
    count = 0
    for i in list:
        if (len(str(i)) <= 2):
            count += 1
        else :
            first = i//100
            second = (i - first*100)//10
            third = i%10
            if ((first - second) == (second - third)) :
                count += 1
    return count

print(hansu(list))
