import sys

n=int(input())

def checkVPS(str_):
    stack=[]
    for char_ in str_:
        if char_=='(': stack.append(char_)
        else:
            if len(stack)!=0: stack.pop()
            else: return print('NO')
            
    if len(stack)==0: return print('YES')
    else: return print('NO')

for _ in range(n):
    checkVPS(sys.stdin.readline().strip())
