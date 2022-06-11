import sys

class Node:
    def __init__(self, value = None, pointer = None):
        self.value = value
        self.pointer = pointer
    
class Stack:
    def __init__(self):
        self.topIt = None
        self.count = 0
    
    def push(self, item):
        self.topIt = Node(item, self.topIt)
        self.count += 1
    
    def size(self):
        print(self.count)
        # return None
    
    def isEmpty(self):
        return (self.count == 0)
    
    def top(self):
        if not self.isEmpty():
            print(self.topIt.value)
            # return None
        else :
            print(-1)
            # return None

    def pop(self):
        if not self.isEmpty():
            node = self.topIt
            self.topIt = node.pointer
            self.count -= 1
            print(node.value)
            # return node.value
        else :
            print(-1)
            # return None
    
    def empty(self):
        if not self.isEmpty():
            print(0)
        else:
            print(1)

n = int(input())

stack = Stack()

for i in range(n):
    word = sys.stdin.readline().split()

    if (word[0] == 'top'):
        stack.top()
    elif (word[0] == 'size'):
        stack.size()
    elif (word[0] == 'empty'):
        stack.empty()
    elif (word[0] == 'pop'):
        stack.pop()
    else:
        stack.push(int(word[1]))
        