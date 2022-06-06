# Node를 사용한 Stack 구현하기

from turtle import st


class Node:
    def __init__(self, value = None, pointer = None):
        self.value = value
        self.pointer = pointer

class Stack:
    def __init__(self):
        self.top = None
        # Stakc의 맨 뒤 (맨 마지막에 push된 데이터)
        self.size = 0
        # 스택의 데이터 개수

    def push(self, item):
        self.top = Node(item, self.top)
        # 새로운 Node 생성, top 이동
        self.size += 1

    def printStack(self):
        node = self.top
        while node:
            print(node.value, end = ' ')
            node = node.pointer
        print()

    def isEmpty(self):
        return (self.size == 0)

    def pop(self):
        # top의 데이터를 꺼내어 리턴(스택에서 제거)
        if not self.isEmpty():
            node = self.top
            self.top = node.pointer # top을 다른 노드로 이동
            self.size -= 1 
            return node.value
        else :
            print('스택이 비었습니다.')
            return None

    def getSize(self):
        return self.size
    
    def peek(self):
        # top의 데이터 리턴(스택에서 제거x)
        if not self.isEmpty():
            return self.top.value
        else:
            print('스택이 비어있습니다.')
            return None
    



stack = Stack()

for i in range(10):
    stack.push(i)

stack.printStack()
# 9 8 7 6 5 4 3 2 1 거꾸로 출력됨 (stack이기 때문)
stack.pop()
# 9를 제거
x = stack.pop()
# 8을 제거하면서 x로 받음
print(x)
# 8 출력
stack.printStack()
# 7 6 5 4 3 2 1 0 출력

x = stack.peek()
# 맨 위에있는 7을 x로 리턴받음(삭제하지는 않음)
stack.printStack()
# 7 6 5 4 3 2 1 0 출력

print(stack.getSize())
# 크기 8




