
import sys
from collections import deque

input = sys.stdin.readline


def getMinArivalTime(r, c, maps, locD, locS, locW):
    minArivalTime = 0
    while 1:
        minArivalTime += 1
        locW = makeWaterExpand(r, c, maps, locD, locS, locW)

        checkArival, locS = makeNextS(r, c, maps, locD, locS, locW)
        if checkArival:
            break
        if not locS:
            return "KAKTUS"

    return minArivalTime


def makeWaterExpand(r, c, maps, locD, locS, locW):
    newQueue = deque([])
    while locW:
        rIdx, cIdx = locW.popleft()
        for nr, nc in [
            (rIdx - 1, cIdx),
            (rIdx + 1, cIdx),
            (rIdx, cIdx - 1),
            (rIdx, cIdx + 1),
        ]:
            if 0 <= nr < r and 0 <= nc < c and maps[nr][nc] == ".":
                maps[nr][nc] = "*"
                newQueue.append((nr, nc))
    return newQueue


def makeNextS(r, c, maps, locD, locS, locW):
    newQueue = deque([])
    checkArival = False

    while locS:
        rIdx, cIdx = locS.popleft()
        for nr, nc in [
            (rIdx - 1, cIdx),
            (rIdx + 1, cIdx),
            (rIdx, cIdx - 1),
            (rIdx, cIdx + 1),
        ]:
            if 0 <= nr < r and 0 <= nc < c:
                if maps[nr][nc] == "D":
                    checkArival = True
                    return checkArival, newQueue

                if maps[nr][nc] == ".":
                    maps[nr][nc] = "S"
                    newQueue.append((nr, nc))

    return checkArival, newQueue


r, c = map(int, input().split())

maps = [[] for _ in range(r)]
locS = deque([])
locW = deque([])
for row in range(r):
    rowData = input().strip()
    for col in range(c):
        maps[row].append(rowData[col])
        if rowData[col] == "D":
            locD = (row, col)
        if rowData[col] == "S":
            locS.append((row, col))
        if rowData[col] == "*":
            locW.append((row, col))

minArivalTime = getMinArivalTime(r, c, maps, locD, locS, locW)

print(minArivalTime)
