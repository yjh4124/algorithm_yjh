
import sys
from collections import deque

input = sys.stdin.readline


def getTimeEnd(n, apples, controls):
    snakes = deque([(1, 1)])
    # 상, 우, 하, 좌
    # ((-1, 0), (0, 1), (1, 0), (0, -1))
    direction = (0, 1)
    time = 0

    while 1:
        time += 1
        nextRow = snakes[-1][0] + direction[0]
        nextCol = snakes[-1][1] + direction[1]
        nextHead = (nextRow, nextCol)

        if nextRow >= 1 and nextRow <= n and nextCol >= 1 and nextCol <= n:
            if nextHead not in snakes:
                snakes.append(nextHead)
            else:
                break
        else:
            break

        direction = getNextDirection(direction, time, controls)

        if nextCol not in apples[nextRow]:
            snakes.popleft()
        else:
            del apples[nextRow][nextCol]

    timeEnd = time
    return timeEnd


def getNextDirection(direction, time, controls):
    if time in controls:
        if controls[time] == "L":
            direction = (
                direction[0] * 0 + direction[1] * -1,
                direction[0] * 1 + direction[1] * 0,
            )
        elif controls[time] == "D":
            direction = (
                direction[0] * 0 + direction[1] * 1,
                direction[0] * -1 + direction[1] * 0,
            )
    nextDirection = direction
    return nextDirection


n = int(input())
k = int(input())
apples = [{} for _ in range(101)]
for _ in range(k):
    appleX, appleY = map(int, (input().split()))
    apples[appleX][appleY] = 1

l = int(input())
controls = {}
for _ in range(l):
    time, command = input().split()
    controls[int(time)] = command

timeEnd = getTimeEnd(n, apples, controls)

print(timeEnd)
