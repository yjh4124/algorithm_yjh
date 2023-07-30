from collections import deque
n,k=map(int,input().split())

que=deque([i for i in range(1, n+1)])
ls=[]

# print(que)

while 1:
    if len(que)==0:
        break
    
    ls.append(que[k-1])
    que.remove(que[k-1])
    que.rotate(-(k-1))
    # print(f'{que} {ls}')

    if len(que)==k-1:
        for i in range(len(que)):
            que.rotate(-(k-1))
            ls.append(que.popleft())

print('<', end='')
print(*ls, sep=', ',end='')
print('>', end='')