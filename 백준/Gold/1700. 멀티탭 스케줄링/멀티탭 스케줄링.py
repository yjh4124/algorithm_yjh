
import sys

input = sys.stdin.readline

hole_num, item_num = map(int, input().split())
item_order = list(map(int, input().split()))

current_items = {}
occupied = [0]
change_num = [0]


def use_new_item(item):
    current_items[item] = 1
    occupied[0] += 1


def is_need_change(item):
    if item in current_items:
        return False
    return True


def find_remove_item(idx):
    next_items = item_order[idx + 1 :]
    max_idx = 0

    for item, _ in current_items.items():
        if item in next_items:
            max_idx = max(max_idx, next_items.index(item))
            continue
        return item
    else:
        remove_item = next_items[max_idx]

    return remove_item


def change_item(item, remove_item):
    del current_items[remove_item]
    current_items[item] = 1
    change_num[0] += 1


for idx, item in enumerate(item_order):
    if occupied[0] < hole_num:
        if is_need_change(item):
            use_new_item(item)
    else:
        if is_need_change(item):
            remove_item = find_remove_item(idx)
            change_item(item, remove_item)

print(change_num[0])
