import sys
t = int(input())

class Node:
    def __init__(self, value = None, pointer = None):
        self.value = value
        self.pointer = pointer

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0
    
    def push(self, item):
        self.top = Node(item, self.top)
        self.size += 1
    
    def pop(self):
        if not self.isEmpty():
            node = self.top
            self.top = node.pointer
            self.size -= 1
            return node.value
        else:
            return None

    def isEmpty(self):
        return (self.size == 0)

for i in range(t):
    word = list(sys.stdin.readline().strip())
    stack = Stack()
    for j in range(len(word)):
        if word[j] == '(':
            stack.push(word[j])
        elif word[j] == ')':
            if stack.isEmpty():
                print("NO")
                break
            else :
                stack.pop()
    else :
        if stack.isEmpty():
            print("YES")
        else :
            print("NO")
