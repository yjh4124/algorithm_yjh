import sys

from collections import deque
n=int(sys.stdin.readline())

que=deque([i for i in range(1,n+1)])


while 1:
    if len(que)==1:
        print(que[0])
        break

    que.popleft()
    temp=que.popleft()
    
    que.append(temp)

    # print(que)