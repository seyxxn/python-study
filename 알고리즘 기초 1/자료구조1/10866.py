from collections import deque
import sys

n = int(input())
dequeList = deque([])

for i in range(n):
    word = sys.stdin.readline().split()
    if word[0] == 'push_back':
        dequeList.append(int(word[1]))
    elif word[0] == 'push_front':
        dequeList.appendleft(int(word[1]))
    elif word[0] == 'pop_front' and len(dequeList) != 0 :
        print(dequeList[0])
        dequeList.popleft()
    elif word[0] == 'pop_front' and len(dequeList) == 0 :
        print(-1)
    elif word[0] == 'pop_back' and len(dequeList) != 0 :
        print(dequeList[-1])
        dequeList.pop()
    elif word[0] == 'pop_back' and len(dequeList) == 0 :
        print(-1)
    elif word[0] == 'size':
        print(len(dequeList))
    elif word[0] == 'empty' and len(dequeList) != 0:
        print(0)
    elif word[0] == 'empty' and len(dequeList) == 0 :
        print(1)
    elif word[0] == 'front' and len(dequeList) != 0:
        print(dequeList[0])
    elif word[0] == 'front' and len(dequeList) == 0:
        print(-1)
    elif word[0] == 'back'  and len(dequeList) != 0:
        print(dequeList[-1])
    elif word[0] == 'back'  and len(dequeList) == 0:
        print(-1)