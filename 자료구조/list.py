# Node
class Node(object):
    def __init__(self, value=None, pointer=None):
        self.value = value       # 값 (데이터)
        self.pointer = pointer   # 다음 노드를 가리키는 포인터
        
    def getData(self):
        return self.value
    
    def getNext(self):
        return self.pointer
    
    def setData(self, newdata):
        self.value = newdata
        
    def setNext(self, newpointer):
        self.pointer = newpointer
    
    def __repr__(self):
        return "[%s -> %s]" % (str(self.value), str(self.pointer))

# assert(조건식)
# 조건식이 거짓이면 AssertionError 발생

# assert(10 == 10)  # 참일때는 그냥 넘어감

# LinkedList 구현
class LinkedListFIFO(object):
    def __init__(self):
        self.head = None    # 리스트의 첫번째 노드를 가리키는 포인터
        self.length = 0     # 리스트의 노드(데이터) 개수 
        self.tail = None   # 리스트의 마지막 노드를 가리키는 포인터
        
    # 새 node를 추가하기
    # tail이 있다면 tail의 다음 node는 새 node를 가리키고 tail은 새 node를 가리킨다.
    def _add(self, value):
        self.length += 1     # 노드 개수 +1 증가
        node = Node(value)   # 새로이 추가될 노드 생성
        if self.tail:
            self.tail.pointer = node     # 새 노드가 기존 tail 뒤에 연결
        self.tail = node     # tail은 뒤에 추가된 새 노드를 가리키게 이동
        
    # 새 노드 추가
    def addNode(self, value):
        if not self.head:       # 첫번째 추가되는 노드라 head가 None이었다면
            self.length = 1
            node = Node(value)
            self.head = node    # 첫번째 노드이기에 head, tail 똑같이 새 노드를 가리킴
            self.tail = node
        else:
            self._add(value)
            
    # head부터 시작하여 각 node의 값을 출력하기
    def _printList(self):
        node = self.head
        while node:          # 맨 끝의 node에 다다를때까지 (가장 마지막에는 None)
            print(node.value, end = " ")
            node = node.pointer   # node를 다음 노드로 이동
        print()
        
    # 리스트 안의 노드 전부 삭제
    def _deleteAll(self):
        self.length = 0
        self.head = None
        self.tail = None
        print("연결리스트가 비었습니다.")
        
    # 인덱스로 노드 찾기
    def _find(self, index):
        node = self.head     # head부터 찾기 시작
        prev = None         # 발견한 노드의 이전 노드
        i = 0
        while node and i < index :
            prev = node
            node = node.pointer
            i += 1
        return node, prev, i
    
    # 값으로 노드 찾기
    def _find_by_value(self, value):
        prev = None
        node = self.head
        found = False        # 찾았는지 여부
        while node and not found:
            if node.value == value:    # 노드 값 비교
                found = True
            else :
                prev = node
                node = node.pointer    # 못찾았으면 다음 노드로 이동
        return node, prev, found
    
    # index에 해당하는 노드를 삭제하기
    def deleteNode(self, index):
        if not self.head or not self.head.pointer:
            # 노드가 없거나 하나밖에 없는 상황
            self.length = 0
            self.head = None
            self.tail = None
            print("LinkedList가 비어졌습니다.")
        else:
            # 노드가 두 개 이상인 경우
            node, prev, i = self._find(index)
            if i == index and node:    # index번째 노드가 존재했다면
                self.length -= 1
                if i == 0 or not prev:   # 첫번째 노드였다면
                    self.head = node.pointer
                else:
                    prev.pointer = node.pointer    # node 삭제
            else:
                print("인덱스{0}에 해당하는 노드가 없습니다." .format(index))
        
    # 특정 value의 노드를 삭제하기
    def deleteNodeByValue(self, value):
        if not self.head or not self.head.pointer:
            self.length = 0 
            self.head = None
            self.tail = None
            print("LinkeList가 비었습니다.")
        else:
            node, prev, i = self._find_by_value(value)
            if node and node.value == value:    # value를 가진 노드가 있다면!
                self.length -= 1
                if i == 0 or not prev:
                    self.head = node.pointer
                    self.tail = node.pointer
                else:
                    prev.pointer = node.pointer
                
            else:
                print("값 {0}에 해당하는 노드가 없습니다.".format(value))
                
    # index 번째 노드 삽입 ()
    def insert(self, index, value):
        node, prev, found = self._find(index)
        self.length += 1
        newNode = Node(value, node)
        
        # 맨 뒤에 insert되는 경우
        if not self.tail or self.tail == node:
            self.tail = newNode
  
        # 맨 앞에 insert되는 경우
        if not prev:
            self.head = newNode
        else:
            prev.pointer = newNode


# list.insert() vs LinkedList.insert()
import time
from datetime import timedelta

num = 40000

start_time = time.time()

data = []
for i in range(num, 0, -1):
    data.insert(0, i)
    
end_time = time.time()
elapsed_time = end_time - start_time  # 경과시간
print("insert() x %d 경과시간 %s" % (num, str(timedelta(seconds = elapsed_time))))

start_time = time.time()

ll = LinkedListFIFO()
for i in range(num, 0, -1):
    ll.insert(0, i)
    
end_time = time.time()
elapsed_time = end_time - start_time  # 경과시간
print("LinkedList의 insert() x %d 경과시간 %s" % (num, str(timedelta(seconds = elapsed_time))))

# LinkedList에서의 insert가 훨씬 빠름


