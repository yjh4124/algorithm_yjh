import sys
from collections import deque

n=int(input())

m=int(input())

data=[]

for _ in range(m):
    x, y, k=map(int, input().split())
    data.append((x, y, k))

# for i in data[:m//2]:
#     print(i, end='')
# print()
# for i in data[m//2:]:
#     print(i, end='')
# print()

graph=[[] for _ in range(n+1)]

degree=[0 for _ in range(n+1)]

# for i in graph:
#     print(i)

for x, y, k in data:
    graph[y].append([x,k])
    degree[x]+=1

# print(degree)
check_root=degree.count(0)-1
# print(check_root)
# print(graph)

queue=deque()

for i in range(1,len(degree)):
    if degree[i]==0:
        queue.append(i)

# print(queue)

cost=[[0]*check_root for _ in range(n+1)]

cnt=0
id=[]
for i in range(1,len(degree)):
    if degree[i]==0:
        id.append(i)
        cost[i][cnt]=1
        cnt+=1

# print(cost)
# cnt=0
while queue:
    # cnt+=1
    part=queue.popleft()
    
    for assy, ea in graph[part]:
        for j in range(check_root):
            cost[assy][(j)%check_root]+=cost[part][(j)%check_root]*ea
        degree[assy]-=1
        if degree[assy]==0:
            queue.append(assy)

    # print(degree)
    # print(queue)
    # print(cost)
    

    # if cnt==7: break

for i in range(len(cost[n])):
    print(f'{id[i]} {cost[n][i]}')
