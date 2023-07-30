import sys
n=int(input())
stack=[0 for _ in range(n+1)]
ptr=0

def push(stack, num):
    global ptr
    ptr+=1
    stack[ptr]=num
    

def pop(stack):
    global ptr
    if ptr!=0: 
        print(stack[ptr])
        ptr-=1
    else: print(-1)

def size(stack):
    global ptr
    print(ptr)

def empty(stack):
    global ptr
    if ptr==0: print(1)
    else: print(0)

def top(stack):
    global ptr
    if ptr==0: print(-1)
    else: print(stack[ptr])
    
for _ in range(n):
    cmd=sys.stdin.readline().split()

    if cmd[0] == 'push': push(stack, int(cmd[1]))
    elif cmd[0] == 'pop': pop(stack)
    elif cmd[0] == 'size': size(stack)
    elif cmd[0] == 'empty': empty(stack)
    else: top(stack)