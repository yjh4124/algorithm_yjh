import sys

n=int(sys.stdin.readline())

data=[0]
data+=list(map(int, sys.stdin.readline().strip()))
edge=[]

for _ in range(n-1):
    u, v=map(int,sys.stdin.readline().split())
    edge.append((u, v))


graph=[[] for _ in range(n+1)]

for u, v in edge:
    graph[u].append(v)
    graph[v].append(u)

cnt=0
def dfs(start):
    global cnt
    for next in graph[start]:
        if visit[next]==0:
            visit[next]=1
            
            if data[next]==1:
                cnt+=1
                continue
            elif data[next]!=1:
                dfs(next)


for start in range(1, len(data)):
    if data[start]==1:
        visit=[0]*(n+1)
        visit[start]=1
        dfs(start)

print(cnt)