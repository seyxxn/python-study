numbers = list(map(int, input().split()))

if (numbers[0] == numbers[1] and numbers[1] == numbers[2]):
    result = 10000 + numbers[0]*1000
elif (numbers[0] == numbers[1]):
    result = 1000 + numbers[0]*100
elif (numbers[0] == numbers[2]):
    result = 1000 + numbers[0]*100
elif (numbers[1] == numbers[2]):
    result = 1000 + numbers[1]*100
else :
    result = max(numbers) * 100
    
print(result)