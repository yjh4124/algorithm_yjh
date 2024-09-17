
import sys

input = sys.stdin.readline

from collections import deque

n = int(input())


for _ in range(n):
    col, row, cabbage_num = map(int, input().split())
    data = [[0] * col for _ in range(row)]

    for _ in range(cabbage_num):
        c, r = map(int, input().split())
        data[r][c] = 1

    visit = [[0 for _ in range(col)] for _ in range(row)]

    dx = (-1, 0, 1, 0)
    dy = (0, 1, 0, -1)

    result = []

    queue = deque()

    for x in range(row):
        for y in range(col):
            cnt = 0

            if visit[x][y] == 0:
                visit[x][y] = 1

                if data[x][y] == 0:
                    continue
                elif data[x][y] == 1:
                    queue.append((x, y))

                    while queue:
                        tmp_x, tmp_y = queue.popleft()

                        cnt += 1

                        for idx in range(4):
                            nx = tmp_x + dx[idx]
                            ny = tmp_y + dy[idx]
                            if 0 <= nx <= row - 1 and 0 <= ny <= col - 1:
                                if visit[nx][ny] == 0:
                                    visit[nx][ny] = 1
                                    if data[nx][ny] == 1:
                                        queue.append((nx, ny))

                    result.append(cnt)

            elif visit[x][y] == 1:
                continue

    print(len(result))
