# 탐색(Search)
# 데이터를 검색하여 찾는 것을 의미

# 탐색 유형
# 1. 순차 탐색(Sequential Search)
# 2. 이진 탐색(Binary Search)

# 순차 탐색
# 동일한 데이터를 찾을 때 까지 선형 자료 구조의 첫번째 데이터부터 마지막 데이터까지 순차적으로 탐색합니다.
# 시간 복잡도는 O(n)
# 찾고자하는 값이 마지막에 위치하거나 데이터가 없는 경우에는 최대 N번만큼 탐색을 실시함

seq1 = []
seq2 = []
for i in range(1, 10000000):
    seq1.append(i) # 오름차순 정렬
    seq2.append(10000000-i) # 내림차순 정렬

def sequentialSearch(seq, value):
    for i in range(len(seq)):
        if seq[i] == value:
            return i
    return None

# print(sequentialSearch(seq1, 9999999))
# print(sequentialSearch(seq2, 9999999))

# 시간 체크 함수
import time
from datetime import timedelta

# func의 수형시간 체크
def checkTime(func, seq, value, title = ''):
    start = time.time()
    func(seq, value)
    end = time.time()
    print(f'{title}: value = {value} 경과시간 {str(timedelta(seconds = end - start))}')

# for cnt in [10000,100000,1000000,10000000]:
#     checkTime(sequentialSearch, seq1, cnt, '오름차순 정렬된 배열 순차 탐색')
#     checkTime(sequentialSearch,  seq2, cnt, '오름차순 정렬된 배열 순차 탐색')
#     print()

# 이진 탐색
# 정렬되어있는 자료구조에서 사용할 수 있는 탐색 알고리즘 입니다.
# 시간 복잡도는 O(logN)
# 최악의 경우 logN번만큼 연산을 수행

def binarySearch(seq, value):
    # 시작 인덱스와 끝 인덱스
    start = 0 
    end = len(seq) - 1
    while start <= end:
        mid = (start + end) //2
        if seq[mid] < value :
            start = mid + 1
        elif seq[mid] > value :
            end = mid - 1
        else :
            return mid

print(binarySearch(seq1, 100))
print(binarySearch(seq1, 10000))
print(binarySearch(seq1, 1000000))

for cnt in [10000,100000,1000000]:
    checkTime(binarySearch, seq1, cnt, '오름차순 정렬된 배열 이진탐색')
    print()