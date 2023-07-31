import sys
sys.setrecursionlimit(10**9)
n=int(input())

graphList=[[] for _ in range(n+1)]

def getGraph():
    for _ in range(n-1):
        node1, node2=map(int, sys.stdin.readline().split())
        graphList[node1].append(node2)
        graphList[node2].append(node1)

getGraph()

visited=[0 for _ in range(n+1)]
visited[1]=1

def findNodeParent(parent):
    for child in graphList[parent]:
        if visited[child]==0: 
            visited[child]=parent
            findNodeParent(child)            

findNodeParent(1)

for idx in range(2, n+1):
    print(visited[idx])
