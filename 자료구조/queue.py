# 큐(Queue)
# 1. 데이터가 들어온 순서대로 추출
# 2. FIFO

# 실생활에서의 큐 -> 줄서는 것

# Queue의 메소드
# enqueue : 큐 뒤쪽에 데이터 삽입
# dequeue : 큐 앞쪽의 데이터 리턴하고 제거
# peek/front : 큐 앞쪽의 항목 조회
# isEmpty : 큐가 비어있는지 확인
# size : 큐의 크기 확인

# 라이브러리를 활용한 큐 구현

from collections import deque
queue = deque([])
print(queue)

queue.append(1) # enqueue
queue.append(2)
print(queue)

x = queue.popleft() # dequeue
print(queue, x)


print('----------')

# Node를 사용한 큐 구현
class Node:
    def __init__(self, value = None, pointer = None):
        self.value = value
        self.pointer = pointer

class LinkedQueue:
    def __init__(self):
        self.head = None # front
        self.tail = None # back
        self.count = 0 # 데이터 개수

    def enqueue(self, value):
        newNode = Node(value)
        if not self.tail: # 첫 데이터인 경우
            self.head = newNode
            self.tail = newNode
        else : # 첫 데이터가 아닌 경우
            self.tail.pointer = newNode # tail 뒤에 newNode 붙이기
            self.tail = newNode # tail 이동

        self.count += 1 # 데이터의 개수 추가

    def printQueue(self):
        node = self.head
        while node:
            print(node.value, end = ' -> ')
            node = node.pointer
        print("None")

    def isEmpty(self):
        return not bool(self.head) # (self.count == 0)

    def dequeue(self):
        if not self.isEmpty(): # 데이터가 존재한다면
            value = self.head.value
            self.head = self.head.pointer # head 이용
            self.count -= 1
            return value
        else:
            print("큐가 비었습니다.")
            return None
    
    def getSize(self):
        return self.count

    def peek(self):
        if not self.isEmpty():
            return self.head.value
        else :
            print('큐가 비었습니다.')
            return None

queue = LinkedQueue()
for i in range(10):
    queue.enqueue(i)
queue.printQueue()

print('큐의 크기 : ', queue.getSize())
print('peek() : ', queue.peek()) 
# 제일 처음에 들어온 0 (제거하지는 않음)
print(queue.dequeue())
# 0 꺼내기
print(queue.dequeue())
# 1 꺼내기
print(queue.dequeue())
# 2 꺼내기
queue.printQueue()