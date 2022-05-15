word = list(str(input()))

if list(reversed(word)) == word:
    print(1)
else:
    print(0)

# 이거왜안돼
# word = input()
# half = len(word)//2

# if len(word)==1:
#     print(1)
# else :
#     for i in range(half):
#         if word[i] != word[len(word)-i-1]:
#             print(0)
#             break
#         print(1)
#         break