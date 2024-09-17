
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**8)

k = int(input())


def is_bipartite_graph(v, graph):
    visit = group = [0] * (v)

    def dfs(node):
        for child in graph[node]:
            if visit[child] == 0:
                visit[child] = 1
                group[child] = -group[node]
                if not dfs(child):
                    return False

            elif group[child] == group[node]:  # 같은 그룹이면 False 반환
                return False

        return True

    for j in range(v):
        if graph[j] and visit[j] == 0:
            group[j] = 1
            visit[j] = 1
            if not dfs(j):
                return False

    return True


for _ in range(k):
    v, e = map(int, input().split())

    graph = [[] for _ in range(v)]

    for _ in range(e):
        a, b = map(int, sys.stdin.readline().split())
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)

    print("YES") if is_bipartite_graph(v, graph) else print("NO")
