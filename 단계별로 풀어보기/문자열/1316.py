n = int(input()) # 입력받을 단어의 개수
count = n
# 똑같은 알파벳이라면, 붙어서 나와야함 -> 그룹단어
# 모두 다 다른 알파벳이라면 -> 그룹단어 인정

for i in range(n):
    word = input()
    if len(word) == len(set(word)):
        # 모두 다 다른 알파벳이라면 -> 그룹단어 인정
        pass
    else :
        # 중복되는 알파벳이 있는 경우
        # 똑같은 알파벳은 붙어서(연속하여) 나와야함 -> 그룹단어
        for i in range(len(word)-1):
            if word.find(word[i]) > word.find(word[i+1]):
                count -= 1
                break

print(count)
