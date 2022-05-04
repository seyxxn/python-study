while(True):
    numbers = []
    n = int(input())
    if n == -1 :
        break
    else :
        for i in range(1,n):
            if n % i == 0 :
                numbers.append(i)
        if sum(numbers) == n :
            print(n,"= ",end="")
            for i in range(0,len(numbers)):
                    if i == len(numbers)-1 :
                        print(numbers[i])
                    else :
                        print(numbers[i],"+", end=" ")
        else :
            print(n,"is NOT perfect.")