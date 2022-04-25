# def isNotSelfNum(n):
#     numList = [int(i) for i in range(1,n+1)]
#     for x in numList:
#         if len(str(x)) == 1:
#             if (x + int(str(x)[0]) == x):
#                 print(x)
#                 # return True 
#         elif len(str(x)) == 2:
#             if (x + int(str(x)[0]) + int(str(x)[1]) == x):
#                 print(x)
#                 # return True        
#         elif len(str(x)) == 3:
#             if (x + int(str(x)[0]) + int(str(x)[1]) + int(str(x)[2]) == x):
#                 print(x)
#                 # return True  
#         elif len(str(x)) == 4:
#             if (x + int(str(x)[0]) + int(str(x)[1]) + int(str(x)[2]) + int(str(x)[3]) == x):
#                 print(x)
#                 # return True  
#         elif len(str(x)) == 5:
#             if (x + int(str(x)[0]) + int(str(x)[1]) + int(str(x)[2]) + int(str(x)[3]) + int(str(x)[4]) == x):
#                 print(x)
#                 # return True
#         # return False


# isNotSelfNum(100)

# numList = [int(i) for i in range(1,100)]

numList = [int(i) for i in range(1,101)]

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

def isNotSelfNum():
    for x in numList:
        if len(str(x)) == 1:
            for y in range(1,x):
                if (plusNum(y) == x):
                    print(x)
        elif len(str(x)) == 2:
            for y in range(1,x):
                if (plusNum(y) == x):
                    print(x)
        elif len(str(x)) == 3:
            for y in range(1,x):
                if (plusNum(y) == x):
                    print(x)
        elif len(str(x)) == 4:
            for y in range(1,x):
                if (plusNum(y) == x):
                    print(x)
        elif len(str(x)) == 5:
            for y in range(1,x):
                if (plusNum(y) == x):
                    print(x)

isNotSelfNum()