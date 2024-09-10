
import sys

input = sys.stdin.readline

from collections import deque


def count_possible_schedules(n):
    possible_schedules_momo = {}
    for i in range(n):
        for j in range(n):
            if i == 0 and j == 0 or i + j > n:
                continue

            initial_state = (i, j)
            initial_log = "w"
            log_memo = set(initial_log)
            possible_schedules_cnt = 0

            queue = deque([(initial_state, initial_log)])

            while queue:
                (w_cnt, h_cnt), log = queue.popleft()

                if (w_cnt, h_cnt) in possible_schedules_momo:
                    possible_schedules_cnt += possible_schedules_momo[(w_cnt, h_cnt)]
                    continue
                
                for drug in ["w", "h"]:
                    new_log = None
                    if drug == "w" and w_cnt:
                        new_state = (w_cnt - 1, h_cnt + 1)
                        new_log = log + "w"

                    elif drug == "h" and h_cnt:
                        new_state = (w_cnt, h_cnt - 1)
                        new_log = log + "h"

                    if new_log and new_log not in log_memo:
                        if new_state == (0, 0):
                            possible_schedules_cnt += 1
                        else:
                            queue.append((new_state, new_log))
                            log_memo.add(new_log)

            possible_schedules_momo[initial_state] = possible_schedules_cnt
    return possible_schedules_momo.get((n - 1, 1), 1)


while 1:
    n = int(input())
    if n == 0:
        break

    print(count_possible_schedules(n))
