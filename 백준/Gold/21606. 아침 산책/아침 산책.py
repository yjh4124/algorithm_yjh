import sys

n=int(sys.stdin.readline())

data=[0]
data+=list(map(int, sys.stdin.readline().strip()))
# print(data)

edge=[]

for _ in range(n-1):
    u, v=map(int,sys.stdin.readline().split())
    edge.append((u, v))

# print(edge)

graph=[[] for _ in range(n+1)]
# print(graph)

for u, v in edge:
    graph[u].append(v)
    graph[v].append(u)

# print(graph)
cnt=0
def dfs(start,root):
    global cnt
    for next in graph[start]:
        if visit[next]==0:
            visit[next]=1
            
            if data[next]==1:
                # print(*root,end=' ')
                # print(next)
                cnt+=1
                continue
            elif data[next]!=1:
                root.append(next)
                dfs(next,root)

    root.pop()
        # elif visit[next]==1:
        #     continue

for start in range(1, len(data)):
    # print(start)
    if data[start]==1:
        visit=[0]*(n+1)
        root=[]
        visit[start]=1
        root.append(start)
        dfs(start,root)
        # print()
    

        # print(visit)

print(cnt)