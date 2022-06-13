from collections import deque
import sys

n = int(input())
queue = deque([])

for i in range(n):
    word = sys.stdin.readline().split()
    if word[0] == 'push':
        queue.append(int(word[1]))
    elif word[0] == 'pop' and len(queue) != 0:
        print(queue[0])
        queue.popleft()
    elif word[0] == 'pop' and len(queue) == 0 :
        print(-1)
    elif word[0] == 'size':
        print(len(queue))
    elif word[0] == 'empty' and len(queue) != 0:
        print(0)
    elif word[0] == 'empty' and len(queue) == 0 :
        print(1)
    elif word[0] == 'front' and len(queue) != 0:
        print(queue[0])
    elif word[0] == 'front' and len(queue) == 0:
        print(-1)
    elif word[0] == 'back'  and len(queue) != 0:
        print(queue[-1])
    elif word[0] == 'back'  and len(queue) == 0:
        print(-1)