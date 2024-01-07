
import sys
from collections import deque

input = sys.stdin.readline


def getTimeEnd(n, apples, controls):
    snake_set = set([(1, 1)]) 
    snakes = deque([(1, 1)])
    direction = (0, 1)
    time = 0

    while True:
        time += 1
        nextRow, nextCol = snakes[-1][0] + direction[0], snakes[-1][1] + direction[1]
        nextHead = (nextRow, nextCol)

        if 1 <= nextRow <= n and 1 <= nextCol <= n and nextHead not in snake_set:
            snakes.append(nextHead)
            snake_set.add(nextHead) 
        else:
            break

        direction = getNextDirection(direction, time, controls)

        if nextCol not in apples[nextRow]:
            tail = snakes.popleft()
            snake_set.remove(tail) 
        else:
            del apples[nextRow][nextCol]

    return time


def getNextDirection(direction, time, controls):
    if time in controls:
        if controls[time] == "L":
            direction = (-direction[1], direction[0])
        elif controls[time] == "D":
            direction = (direction[1], -direction[0])
    return direction


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
