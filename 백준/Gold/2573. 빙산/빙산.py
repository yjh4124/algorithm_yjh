
import sys

input = sys.stdin.readline


def getTimeEndIceberg(n, m, iceberg):
    timeEnd = 0
    while 1:
        numIceberg = getNumIceberg(n, m, iceberg)
        if numIceberg >= 2:
            break
        if numIceberg == 0:
            timeEnd = 0
            break
        timeEnd += 1
        getNextIceberg(n, m, iceberg)

    return timeEnd


def getNextIceberg(n, m, iceberg):
    stack = []

    for i in range(n):
        for j in range(m):
            if iceberg[i][j]:
                cnt = 0
                for ni, mj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                    if 0 <= ni < n and 0 <= mj < m and not iceberg[ni][mj]:
                        cnt += 1
                if cnt > 0:
                    stack.append((i, j, cnt))

    while stack:
        i, j, cnt = stack.pop()
        iceberg[i][j] = max(iceberg[i][j] - cnt, 0)


def getNumIceberg(n, m, iceberg):
    numIceberg = 0
    group = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if iceberg[i][j] and not group[i][j]:
                numIceberg += 1
                if numIceberg >= 2:
                    break
                makeGroupIceberg(n, m, i, j, iceberg, group, numIceberg)
    return numIceberg


def makeGroupIceberg(n, m, ci, cj, iceberg, group, numIceberg):
    stack = [(ci, cj)]
    while stack:
        i, j = stack.pop()
        if group[i][j]:
            continue
        group[i][j] = numIceberg
        for ni, mj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            if 0 <= ni < n and 0 <= mj < m and iceberg[ni][mj] and not group[ni][mj]:
                stack.append((ni, mj))


n, m = map(int, input().split())

iceberg = []

for _ in range(n):
    iceberg.append([int(i) for i in input().split()])

timeEnd = getTimeEndIceberg(n, m, iceberg)
print(timeEnd)
