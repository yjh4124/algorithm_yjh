import sys

n = int(input())
road=tuple(tuple(int(i) for i in sys.stdin.readline().split()) 
           for _ in range(n))
graph = [[0] * n for _ in range(n)]
graph[0][0] = 1 

for i in range(n):
    for j in range(n):

        if j + road[i][j] < n:
            if road[i][j]!=0:
                graph[i][j + road[i][j]] += graph[i][j]


        if i + road[i][j] < n:
            if road[i][j]!=0:
                graph[i + road[i][j]][j] += graph[i][j]

    
print(graph[-1][-1])