import sys
from typing import TypedDict, Optional

input = sys.stdin.readline

class Command(TypedDict):
    type: str
    arg: Optional[str]

class TextEditor:
    def __init__(self, initial_text: str):
        self.left_stack = list(initial_text)
        self.right_stack = []

    def move_left(self):
        if self.left_stack:
            self.right_stack.append(self.left_stack.pop())

    def move_right(self):
        if self.right_stack:
            self.left_stack.append(self.right_stack.pop())

    def delete_left(self):
        if self.left_stack:
            self.left_stack.pop()

    def insert(self, char: str):
        self.left_stack.append(char)

    def get_text(self) -> str:
        return ''.join(self.left_stack + list(reversed(self.right_stack)))

    def execute(self, command: Command):
        match command["type"]:
            case "L": self.move_left()
            case "D": self.move_right()
            case "B": self.delete_left()
            case "P": self.insert(command["arg"])
            case _: pass

def parse_command(line: str) -> Command:
    parts = line.split()
    return {"type": parts[0], "arg": parts[1] if len(parts) > 1 else None}

initial_text = input().strip()
command_count = int(input().strip())

editor = TextEditor(initial_text)

for _ in range(command_count):
    cmd = parse_command(input().strip())
    editor.execute(cmd)

print(editor.get_text())
