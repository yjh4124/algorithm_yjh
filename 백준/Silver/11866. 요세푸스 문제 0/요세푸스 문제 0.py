from collections import deque

n,k=map(int,(input().split()))
queue=deque(i for i in range(1,n+1))
    
def popKth(k):
    print('<', end='')
    while queue:
        queue.rotate(-(k-1))
        print(queue.popleft(),end='')
        if queue: print(', ',end='')
    print('>')

popKth(k)