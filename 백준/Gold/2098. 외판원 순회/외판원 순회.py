
import sys

input = sys.stdin.readline

INF = 10**9
city_num = int(input())
costs = [list(map(int, input().split())) for _ in range(city_num)]
min_total_cost_memo = {}


def move_cost(start, next_):
    return costs[start][next_]


def is_travel_complete(visited_bitmask):
    return visited_bitmask == (1 << city_num) - 1


def is_unvisited(visited_bitmask, next_city):
    return not visited_bitmask & 1 << next_city


def dfs_travel(city, visited_bitmask):
    global min_total_cost_memo
    if is_travel_complete(visited_bitmask):
        travel_cost = move_cost(city, 0)
        return travel_cost if travel_cost else INF

    if min_total_cost_memo.get((city, visited_bitmask), None) is not None:
        return min_total_cost_memo[(city, visited_bitmask)]

    min_total_cost = INF
    for next_city in range(city_num):
        if is_unvisited(visited_bitmask, next_city):
            travel_cost = move_cost(city, next_city)
            if travel_cost:
                new_visited_bitmask = visited_bitmask | 1 << next_city
                min_total_cost = min(
                    min_total_cost,
                    dfs_travel(next_city, new_visited_bitmask) + travel_cost,
                )
    min_total_cost_memo[(city, visited_bitmask)] = min_total_cost

    return min_total_cost


start, visited_bitmask = 0, 1
print(dfs_travel(start, visited_bitmask))
