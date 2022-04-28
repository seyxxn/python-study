word = input()
word = word.lower()
wordNum = [0]*26

for i in range(97,123,1): # 소문자 a-z 순회
    count = 0
    for j in word : # word 순회
        if (j == chr(i)):
            count += 1
            wordNum[i-97] = count

maxNum = max(wordNum)
if wordNum.count(maxNum) > 1 :
    print("?")
else :
    maxWordNum = wordNum.index(maxNum) + 97
    print(chr(maxWordNum).upper())