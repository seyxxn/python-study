# def isNotSelfNum(n):
#     list = [[int(i) for i in range(1,n+1)]]
#     for x in list:
#         if len(str(x)) == 1:
#             if (x + int(str(x)[0]) == x):
#                 print(x)
#                 return True 
#         elif len(str(x)) == 2:
#             if (x + int(str(x)[0]) + int(str(x)[1]) == i):
#                 print(x)
#                 return True        
#         elif len(str(x)) == 3:
#             if (x + int(str(x)[0]) + int(str(x)[1]) + int(str(x)[2]) == i):
#                 print(x)
#                 return True  
#         elif len(str(x)) == 4:
#             if (x + int(str(x)[0]) + int(str(x)[1]) + int(str(x)[2]) + int(str(x)[3]) == i):
#                 print(x)
#                 return True  
#         elif len(str(x)) == 5:
#             if (x + int(str(x)[0]) + int(str(x)[1]) + int(str(x)[2]) + int(str(x)[3]) + int(str(x)[4]) == i):
#                 print(x)
#                 return True
#         return False


# isNotSelfNum(10000)