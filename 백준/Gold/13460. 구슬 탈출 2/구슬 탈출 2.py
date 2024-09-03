import sys
from collections import deque

input = sys.stdin.readline

rows, cols = map(int, input().split())
board = [[0] * cols for _ in range(rows)]

# 방향 설정 및 매핑
directions = ["up", "right", "down", "left"]
tick_moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
tilt_map = dict(zip(directions, tick_moves))


# 보드 초기화 및 초기 위치 설정
def initialize_board():
    red_pos = blue_pos = (-1, -1)

    for i in range(rows):
        for j, val in enumerate(input().rstrip()):
            board[i][j] = val
            if val == "R":
                red_pos = (i, j)
            elif val == "B":
                blue_pos = (i, j)

    return red_pos, blue_pos


# 보드를 기울였을 때, 새로운 red, blue 위치 반환
def get_new_position(red, blue, tilt):
    di, dj = tilt_map[tilt]
    red_moving = blue_moving = True
    ri, rj = red
    bi, bj = blue

    while red_moving or blue_moving:
        if red_moving:
            ri += di
            rj += dj
        if blue_moving:
            bi += di
            bj += dj

        if red_moving and 0 <= ri < rows and 0 <= rj < cols:
            if board[ri][rj] == "O":
                red = (-1, -1)
                red_moving = False
            elif board[ri][rj] != "#":
                if board[bi][bj] == "#" and ((ri == blue[0]) and (rj == blue[1])):
                    red_moving = False
                else:
                    red = (ri, rj)
            else:
                red_moving = False

        if blue_moving and 0 <= bi < rows and 0 <= bj < cols:
            if board[bi][bj] == "O":
                blue = (-1, -1)
                blue_moving = False

            elif board[bi][bj] != "#":
                if board[ri][rj] == "#" and ((bi == red[0]) and (bj == red[1])):
                    blue_moving = False
                else:
                    blue = (bi, bj)
            else:
                blue_moving = False

    return red, blue


def bfs_escape(red_pos, blue_pos):
    q = deque([[red_pos, blue_pos, 0, tilt] for tilt in tilt_map])
    visited = set()
    visited.add((red_pos, blue_pos))

    while q:
        r, b, tilt_cnt, tilt = q.popleft()

        new_red, new_blue = get_new_position(r, b, tilt)

        if new_red == (-1, -1) and new_blue != (-1, -1):
            return tilt_cnt + 1

        if (
            new_red != (-1, -1)
            and new_blue != (-1, -1)
            and (new_red, new_blue) not in visited
            and tilt_cnt < 9
        ):
            visited.add((new_red, new_blue))
            q.extend([[new_red, new_blue, tilt_cnt + 1, tilt] for tilt in tilt_map])

    return -1


red_start, blue_start = initialize_board()
result = bfs_escape(red_start, blue_start)
print(result)
