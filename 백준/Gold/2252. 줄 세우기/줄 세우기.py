# 입력 받기
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)  # 방문 여부 체크 배열
result = []  # 결과를 담을 리스트, 스택으로 활용

# 모든 간선 정보를 입력받아 그래프를 구성
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# DFS 함수
def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)
    result.append(v)  # 현재 노드 방문 처리 후 결과 스택에 추가

# 모든 노드에 대해 DFS 수행
for i in range(1, n + 1):
    if not visited[i]:
        dfs(i)

# 위상 정렬을 수행한 결과를 역순으로 출력
for i in result[::-1]:
    print(i, end=' ')
