from collections import deque
x = int(input())
queue = deque([])
for i in range(1, x+1):
    queue.append(i)

while len(queue) != 1:
    queue.popleft()
    x = queue.popleft()
    queue.append(x)

print(queue[0])