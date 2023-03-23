import sys
from collections import deque

n,k=map(int, sys.stdin.readline().split())
# print(n, k)

graph=[[0 for _ in range(n+1)] for _ in range(n+1)]

# for i in graph:
#     print(i)
pos=[[0,0]]*(n+1)

init=[]

for i in range(1,n+1):
    data=list(map(int, sys.stdin.readline().split()))
    for j in range(1,len(data)+1):
        graph[i][j]=data[j-1]
        if data[j-1]!=0:
            init.append((data[j-1], (i, j)))

s, xx, yy=map(int, input().split())

# print(s, xx, yy)

# for i in graph:
#     print(i)

queue=deque(sorted(init))
# print(queue)

dx=(1, -1, 0, 0)
dy=(0, 0, 1, -1)

time=0
roof=len(queue)
cnt=0

while queue:
    
    check=0

    vi, (x, y) = queue.popleft()
    

    for i in range(4):
        new_x=x+dx[i]
        new_y=y+dy[i]
        if 1<=new_x<=n and 1<=new_y<=n:
            if graph[new_x][new_y]==0:
                queue.append((vi, (new_x, new_y)))
                graph[new_x][new_y]=vi
    
    cnt+=1
    if cnt==roof:
        time+=1
        cnt=0
        roof=len(queue)
        
    if time==s: 
        break
    

print(graph[xx][yy])