import sys

class Node:
    def __init__(self,value = None, pointer = None):
        self.value = value
        self.pointer = pointer

class Stack:
    def __init__(self):
        self.top = None

    def push(self, item):
        self.top = Node(item, self.top)

    def pop(self):
        node = self.top
        self.top = node.pointer
        print(node.value)

    def printStack(self):
        node = self.top
        while node:
            print(node.value, end="")
            node = node.pointer


words = list(sys.stdin.readline().split()) # 공백을 구분자로, words 리스트에 저장
for j in range(len(words)): # words의 길이 만큼 반복 -> words의 단어(공백으로 구분한)를 각각 뒤집어 출력
    stack = Stack()
    for k in range(len(words[j])):
        stack.push(words[j][k])
    stack.printStack()
    print(" ", end="")
print()