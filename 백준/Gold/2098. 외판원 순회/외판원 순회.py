
import sys

input = sys.stdin.readline

INF = 10**9
city_num = int(input())
costs = [list(map(int, input().split())) for _ in range(city_num)]


# 방문 상태가 mask일 때 마지막 방문 도시가 city일 때의 최소 비용
min_total_cost_memo = [[(INF, "")] * city_num for _ in range(1 << city_num)]

# 각 도시에서 출발하는 비용합 0 으로 설정
for start in range(city_num):
    min_total_cost_memo[1 << start][start] = (0, start)


def move_cost(from_city, to_city):
    return costs[from_city][to_city]


def is_visited(visited_mask, curr_city):
    return visited_mask & 1 << curr_city


def is_unvisited(visited_mask, next_city):
    return not visited_mask & 1 << next_city


def get_min_total_cost():
    min_cost = INF

    for last_city, (last_total_cost, start_city) in enumerate(min_total_cost_memo[-1]):
        if move_cost(last_city, start_city):
            min_cost = min(min_cost, last_total_cost + move_cost(last_city, start_city))

    return min_cost


for visited_mask in range(1 << city_num):
    for curr_city in range(city_num):
        if is_visited(visited_mask, curr_city):
            for next_city in range(city_num):
                if is_unvisited(visited_mask, next_city) and move_cost(
                    curr_city, next_city
                ):
                    new_visited_mask = visited_mask | (1 << next_city)

                    new_total_cost = min_total_cost_memo[visited_mask][curr_city][
                        0
                    ] + move_cost(curr_city, next_city)
                    if (
                        new_total_cost
                        < min_total_cost_memo[new_visited_mask][next_city][0]
                    ):
                        min_total_cost_memo[new_visited_mask][next_city] = (
                            new_total_cost,
                            min_total_cost_memo[visited_mask][curr_city][1],
                        )

print(get_min_total_cost())
