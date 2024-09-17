import sys

input = sys.stdin.readline

n = int(input())

data = [[int(data) for data in sys.stdin.readline().split()] for _ in range(n)]

# 좌표 증가 방향: 우, 상, 좌, 하
dx = (0, -1, 0, 1)
dy = (1, 0, -1, 0)

GRID_SIZE = 101
grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]


def generate_dragon_curves(data):
    for y, x, d, g in data:

        curve_points = [(x, y)]
        curve_points.append((x + dx[d], y + dy[d]))

        grid[x][y] = 1
        grid[x + dx[d]][y + dy[d]] = 1

        for _ in range(g):
            pivot_x, pivot_y = curve_points[-1]

            for i in range(len(curve_points) - 2, -1, -1):
                pre_x, pre_y = curve_points[i]
                new_x = pivot_x + (pre_y - pivot_y)
                new_y = pivot_y - (pre_x - pivot_x)

                if 0 <= new_x <= GRID_SIZE - 1 and 0 <= new_y <= GRID_SIZE - 1:
                    grid[new_x][new_y] = 1
                    curve_points.append((new_x, new_y))


def count_squares():
    cnt = 0
    for col in range(GRID_SIZE - 1):
        for row in range(GRID_SIZE - 1):
            sum_ = (
                grid[row][col]
                + grid[row + 1][col]
                + grid[row][col + 1]
                + grid[row + 1][col + 1]
            )
            if sum_ == 4:
                cnt += 1

    return cnt


generate_dragon_curves(data)
print(count_squares())
