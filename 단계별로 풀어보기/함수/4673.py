def selfNum():
    numList = list(range(1,10001)) # 1-10000 리스트 생성
    notSelfNumList = [] # selfNum이 아닌 숫자를 담을 리스트 생성
    for x in numList : # 1-10000 숫자 순회하기 위한 반복문
        for i in str(x): # 각 숫자를 문자열로 변환하고, 그 문자열을 순회하기 위한 반복문
            x += int(i) # 그 문자열을 각각 더한 값을 x에 저장
        if x <= 10000: # 그 더한 값이 10000보다 작거나 같은 값에 속한다면, 생성자가 있는 숫자임
            notSelfNumList.append(x) # 생성자가 있는 숫자는 selfNum이 아니므로 위에서 만들어둔 리스트에 추가
    for y in set(notSelfNumList): # notSelfNum을 순환한다. 이때, 중복을 제거하기 위해 set으로의 형변환
        numList.remove(y) # numList의 값들 중에서 notSelfNum에 있는 값은 모두 제거한다. selfNum만 남기기 위함
    for z in numList: # 출력
        print(z)

selfNum()