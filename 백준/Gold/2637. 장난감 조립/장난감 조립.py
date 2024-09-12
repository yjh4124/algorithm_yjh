
import sys

input = sys.stdin.readline

from collections import deque


def get_product_costs(num_parts, dependencies):
    graph = [[] for _ in range(num_parts + 1)]
    indegree = [0] * (num_parts + 1)

    # 상위 부품과 하위 부품 간의 의존성 그래프 설정
    for part, base, qty in dependencies:
        graph[base].append((part, qty))
        indegree[part] += 1

    # 기본 부품 찾기
    base_parts = [i for i in range(1, num_parts + 1) if indegree[i] == 0]
    num_base_parts = len(base_parts)

    queue = deque(base_parts)

    # 각 부품의 기본 부품 비용을 저장하는 배열
    cost = [[0] * num_base_parts for _ in range(num_parts + 1)]

    # 기본 부품의 초기 비용 설정
    for idx, part in enumerate(base_parts):
        cost[part][idx] = 1

    # 위상 정렬을 사용한 부품 비용 계산
    while queue:
        current_part = queue.popleft()

        for next_part, qty in graph[current_part]:
            for idx in range(num_base_parts):
                cost[next_part][idx] += cost[current_part][idx] * qty
            indegree[next_part] -= 1
            if indegree[next_part] == 0:
                queue.append(next_part)

    result = [(base_parts[idx], cost[num_parts][idx]) for idx in range(num_base_parts)]
    return result


n = int(input())
m = int(input())
assembly_data = [tuple(map(int, input().split())) for _ in range(m)]


results = get_product_costs(n, assembly_data)
for part, qty in results:
    print(f"{part} {qty}")