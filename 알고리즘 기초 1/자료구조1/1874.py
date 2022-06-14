import sys

class Node:
    def __init__(self, value = None, pointer = None):
        self.value = value
        self.pointer = pointer

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, item):
        node = Node(item, self.top)
        self.size += 1
    
    def pop(self):
        if not self.isEmpty():
            node = self.top
            self.top = self.pointer
            self.size -= 1
            return node.value
        else :
            return None

    def isEmpty(self):
        return (self.size == 0)

    def peek(self):
        if not self.isEmpty():
            return (self.top.value)
        else:
            return None

# stack에 push하는 순서는 반드시 오름차순을 지킨다.
# push 연산은 + 로, pop연산은 -로 표현
# 불가능한 경우는 NO 출력
# 

stack = Stack()
n = int(input())
for i in range(n):
    x = int(input())
    stack.push(x)
