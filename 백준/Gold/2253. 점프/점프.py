import sys

input = sys.stdin.readline

from collections import deque

stone_num, small_stone_num = map(int, input().split())
small_stones = set(int(input()) for _ in range(small_stone_num))
INF = 10**9

# 초기 설정
initial_pos, initial_jump_width, initial_cnt = 1, 1, 0

# 도착 돌멩이 위치, 점프 너비 별 최소 점프 횟수 메모(행: 도착 돌멩이 위치, 열: 점프 너비)
min_cnt_memo = {}


def bfs_jump_stone():
    if stone_num in small_stones:
        return print(-1)

    queue = deque([(initial_pos, initial_jump_width, initial_cnt)])

    while queue:
        pos, jump_width, cnt = queue.popleft()
        next_cnt = cnt + 1

        next_pos = pos + jump_width
        if next_pos == stone_num:
            return print(next_cnt)

        if 1 <= next_pos <= stone_num and next_pos not in small_stones:
            for i in [1, 0, -1]:
                next_jump_width = jump_width + i
                if 1 <= next_jump_width < stone_num:
                    key = (next_pos, next_jump_width)
                    if next_cnt < min_cnt_memo.get(key, INF):
                        min_cnt_memo[key] = next_cnt
                        queue.append((next_pos, next_jump_width, next_cnt))

    return print(-1)


# bfs 돌멩이 점프
bfs_jump_stone()