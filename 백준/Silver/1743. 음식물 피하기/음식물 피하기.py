import sys
from collections import deque

n, m, k = map(int, input().split())

data=[[data for data in map(int,input().split())]
      for _ in range(k)]

# print(data)

graph=[[0 for _ in range(m)] for _ in range(n)]

for r, c in data:
    graph[r-1][c-1]=1

# for i in graph:
#     print(i)

visit=[[0 for _ in range(m)] for _ in range(n)]

result=[]
max_re=0

dx=(-1,0,1,0)
dy=(0,1,0,-1)

queue=deque()

for r in range(n):
    for c in range(m):
        cnt=0
        if visit[r][c]==0:
            visit[r][c]=1
            if graph[r][c]==1:
                cnt+=1
                queue.append((r,c))
                
                while queue:
                    r, c=queue.popleft()
                    for dt in range(4):
                        r+=dx[dt]
                        c+=dy[dt]
                        if 0<=r<=n-1 and 0<=c<=m-1:
                            if visit[r][c]==0:
                                visit[r][c]=1
                                if graph[r][c]==1:
                                    cnt+=1
                                    queue.append((r,c))
                        r-=dx[dt]
                        c-=dy[dt]
                result.append(cnt)
                max_re=max(max_re, cnt)
# print(result)
print(max_re)
