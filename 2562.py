# arr = []
# for i in range(9):
#     arr.append(input())

arr = [int(input()) for x in range(9)]

print(max(arr))
print(arr.index(max(arr))+1)