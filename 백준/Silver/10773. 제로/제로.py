import sys
n=int(input())
stack=[]

def push(stack, num):
    stack.append(num)

def pop(stack):
    stack.pop()

for _ in range(n):
    num=int(sys.stdin.readline())
    if num==0: 
        if len(stack)!=0: pop(stack)
    else: push(stack, num)

print(sum(stack))