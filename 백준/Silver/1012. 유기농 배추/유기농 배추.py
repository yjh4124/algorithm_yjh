
import sys

input = sys.stdin.readline

from collections import deque

n = int(input())


def bfs(x, y):
    global visited, row, col
    visited[x][y] = 1

    queue.append((x, y))

    while queue:
        tmp_x, tmp_y = queue.popleft()
        for idx in range(4):
            nx = tmp_x + dx[idx]
            ny = tmp_y + dy[idx]
            if 0 <= nx <= row - 1 and 0 <= ny <= col - 1:
                if visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    if data[nx][ny] == 1:
                        queue.append((nx, ny))


for _ in range(n):
    col, row, cabbage_num = map(int, input().split())
    data = [[0] * col for _ in range(row)]

    for _ in range(cabbage_num):
        c, r = map(int, input().split())
        data[r][c] = 1

    visited = [[0 for _ in range(col)] for _ in range(row)]

    dx = (-1, 0, 1, 0)
    dy = (0, 1, 0, -1)

    result = []

    queue = deque()

    cnt = 0
    for x in range(row):
        for y in range(col):
            if data[x][y] and not visited[x][y]:
                bfs(x, y)
                cnt += 1

    print(cnt)
