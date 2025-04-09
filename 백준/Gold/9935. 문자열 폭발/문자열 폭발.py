
import sys

input = sys.stdin.readline

def remove_bomb_word(text: str, bomb_word: str) -> str:
    stack = []
    for char in text:
        stack.append(char)
        if len(stack) >= len(bomb_word) and ''.join(stack[-len(bomb_word):]) == bomb_word:
            for _ in range(len(bomb_word)):
                stack.pop()
    return ''.join(stack)

text = input().strip()
bomb_word = input().strip()
print(remove_bomb_word(text, bomb_word) or "FRULA")
