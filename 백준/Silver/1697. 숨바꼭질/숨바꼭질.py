import sys
from collections import deque

n, k=map(int, sys.stdin.readline().split())


queue=deque([n])
time=0

limit=100000
visit=[0]*(limit+1)
visit[n]=1

while queue:

    n=queue.popleft()

    if visit[k] !=0: break
    if n-1>=0:
        if visit[n-1] == 0:
            visit[n-1]=visit[n]+1
            queue.append(n-1)

    if n+1<=limit:
        if visit[n+1] == 0:
            visit[n+1]=visit[n]+1
            queue.append(n+1)

    if n*2<=limit:
        if visit[n*2] == 0:
            visit[n*2]=visit[n]+1
            queue.append(n*2)

    
print(visit[k]-1)