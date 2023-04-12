import sys
from collections import deque

n=int(input())

data=[[int(data) for data in sys.stdin.readline().strip()]
       for _ in range(n)]

# for i in data:
#     print(i)


visit=[[0 for _ in range(n)] for _ in range(n)]

# for i in visit:
#     print(i)

dx=(-1, 0, 1, 0)
dy=(0, 1, 0, -1)

result=[]

queue=deque()

for x in range(n):
    for y in range(n):
        cnt=0

        if visit[x][y]==0:
            visit[x][y]=1

            if data[x][y]==0: continue
            elif data[x][y]==1:
                queue.append((x, y))

                while queue:
                    tmp_x, tmp_y=queue.popleft()

                    cnt+=1

                    for idx in range(4):
                        nx=tmp_x+dx[idx]
                        ny=tmp_y+dy[idx]
                        if 0<=nx<=n-1 and 0<=ny<=n-1:
                            if visit[nx][ny]==0:
                                visit[nx][ny]=1
                                if data[nx][ny]==1:
                                    queue.append((nx,ny))
                
                result.append(cnt)

        elif visit[x][y]==1:
            continue


print(len(result))
for i in sorted(result):
    print(i)



