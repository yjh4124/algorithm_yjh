import sys
from collections import deque

n=int(sys.stdin.readline())
queue=deque(i for i in range(1,n+1))

while 1:
    if len(queue)==1: break
    queue.popleft()
    queue.append(queue.popleft())

print(queue[0])