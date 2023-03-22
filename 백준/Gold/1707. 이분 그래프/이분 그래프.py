import sys

sys.setrecursionlimit(10**8)
k=int(input())

result=True

def dfs(node):
    global result
    for child in graph[node]:
        if visit[child]==None:
            visit[child]=1
            link.append(child)
            group[child]=-group[node]
            dfs(child)

        elif visit[child]!=None:
            if group[child]==group[node]:
                result=False

for _ in range(k):
    result=True
    v, e=map(int, input().split())

    graph=[[] for _ in range(v+1)]

    for _ in range(e):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    visit=[None]*(v+1)
    visit[0]=0
    group=[None]*(v+1)
    group[0]=0
    # check=0
    link=[]
    while None in visit:
        for j in range(1,len(graph)):
            if graph[j]!=[] and visit[j]==None:
                # check=j
                group[j]=1
                visit[j]=1
                link.append(j)
                dfs(j)

            elif graph[j]==[]:
                visit[j]=0
                group[j]=0

    if result==True:
        print('YES')
    else: print('NO')
    # print()

