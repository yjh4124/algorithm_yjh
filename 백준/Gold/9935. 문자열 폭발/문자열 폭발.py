import sys
input = sys.stdin.readline

def remove_bomb(text: str, bomb: str) -> str:
    stack = []
    bomb_len = len(bomb)

    for char in text:
        stack.append(char)
        if len(stack) >= bomb_len and ''.join(stack[-bomb_len:]) == bomb:
            del stack[-bomb_len:] 

    return ''.join(stack) or "FRULA"

text = input().strip()
bomb = input().strip()
print(remove_bomb(text, bomb))