# 정렬 알고리즘
# 1. 삽입정렬
# 2. 선택정렬
# 3. 버블정렬
# 4. 퀵 정렬

# 선택정렬
# 가장 작은 것을 선택해서 제일 앞(왼쪽)에서부터 정렬시킴

from urllib import request


def selectionSort(seq):
    N = len(seq)
    for i in range(N-1): # N-1 만큼 사이클을 돈다
        # i번째 부터 시작해서 끝까지의 최솟값을 찾는다.
        # 최솟값의 위치(min_idx)를 선택한다.
        min_idx = i
        for j in range(i+1, N):
            if seq[min_idx] > seq[j]: # 더 작은 값이 등장 시
                min_idx = j # 최솟값 갱신

        # 선택은 min_idx번째 데이터와 1번째 데이터 교환
        seq[min_idx], seq[i] = seq[i], seq[min_idx]
        print(seq, f'{i+1}번쨰 사이클 이후')
    return seq

print('선택 정렬')
seq = [11,3,28,43,9,4]
seq = selectionSort(seq)
print(seq)

print('----------')

# 삽입 정렬
# 왼쪽부터 알맞은 곳에 데이터를 넣어줌

def insertionSort(seq):
    for i in range(1,len(seq)): # 1부터 len(leq)-1 만큼의 사이클 횟수
        intData = seq[i]
        j = i -1
        while j >= 0: # 삽입할 위치 찾기
            if seq[j] <= intData:
                break
            seq[j+1] = seq[j]
            j -= 1
        seq[j+1] = intData
        print(seq, f'{i}번째 사이클 후')
    return seq

print('삽입정렬')
seq = [11,3,28,43,9,4]
seq = insertionSort(seq)
print(seq)

print('----------')

    
# 버블 정렬
# 주어진 N개의 배열에 대해
# 1. 인접한 두 개의 데이터 비교 (a,b)
# 2. a,b 크기가 반대면 '값 교환' (오름차순의 경우, a>b이면 교환)
# 3. 배열 끝까지 다다를 때까지 1,2번 반복
# 4. 마지막 비교는 N-2와 N-1을 비교
# 5. 3번이 끝나면 맨 끝의 데이터는 가장 큰 값이 될 것이다.
# 6. 이제 N을 1씩 감소하고 N이 1이 될 때까지 1번부터 반복

def bubbleSort(seq):
    length = len(seq) - 1
    for num in range(length, 0 , -1): # cycle 횟수
        for i in range(num): # 비교 횟수
            if seq[i] > seq[i+1] :# 왼쪽이 오른쪽보다 크다면 값을 바꾼다.
                seq[i], seq[i+1] = seq[i+1], seq[i]
        print(seq, f'{length-num+1}번째 사이클 후')
    return seq

print('버블정렬')
seq = [11,3,28,43,9,4]
seq = bubbleSort(seq)
print(seq)
