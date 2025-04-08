
import sys
from typing import TypedDict, Optional

input = sys.stdin.readline

class Command(TypedDict):
    command:str
    value:Optional[str]

class BaseEditor:
    def __init__(self, text: str):
        self.left = list(text)  
        self.right = []         

    def move_cursor_left(self):
        if self.left:
            self.right.append(self.left.pop())

    def move_cursor_right(self):
        if self.right:
            self.left.append(self.right.pop())

    def delete_char(self):
        if self.left:
            self.left.pop()

    def insert_char(self, char: str):
        self.left.append(char)

    def get_text(self) -> str:
        return ''.join(self.left + self.right[::-1])


    def edit(self, command:Command)->None:
        cmd=command['command']
        val=command['value']
        match cmd:
            case 'L':
                self.move_cursor_left()
            case 'D':
                self.move_cursor_right()
            case 'B':
                self.delete_char()
            case 'P':
                self.insert_char(val)
            case _:
                pass


def parse_command(line:str)->Command:
    tokens=line.split()
    return Command(command=tokens[0], value=tokens[1] if len(tokens)>1 else None)


text=input().strip()
command_count=int(input().strip())

editor=BaseEditor(text)

for _ in range(command_count):
    command=parse_command(input().strip())
    editor.edit(command)

print(editor.get_text())







