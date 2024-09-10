
import sys

input = sys.stdin.readline

from collections import deque


def count_possible_schedules(n):
    possible_schedules_momo = {}
    for i in range(n):
        for j in range(n - i + 1):
            state = (i, j)
            log = "w"
            log_memo = set(log)
            schedules_count = 0

            queue = deque([(state, log)])

            while queue:
                (w_cnt, h_cnt), log = queue.popleft()

                if (w_cnt, h_cnt) in possible_schedules_momo:
                    schedules_count += possible_schedules_momo[(w_cnt, h_cnt)]
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
                            schedules_count += 1
                        else:
                            queue.append((new_state, new_log))
                            log_memo.add(new_log)

            possible_schedules_momo[state] = schedules_count
    return possible_schedules_momo.get((n - 1, 1), 1)


while 1:
    n = int(input())
    if n == 0:
        break

    print(count_possible_schedules(n))
