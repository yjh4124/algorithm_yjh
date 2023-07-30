import sys

n=int(input())
queue=[0 for _ in range(n)]
ptrL=0
ptrR=0

def push(queue, num):
    global ptrL
    global ptrR
    if ptrR==n: ptrR=0
    queue[ptrR]=num
    ptrR+=1
    

def pop(queue):
    global ptrL
    global ptrR
    if ptrL!=ptrR: 
        if ptrL==n: ptrL=0
        print(queue[ptrL])
        ptrL+=1
    else: print(-1)

def size(queue):
    global ptrL
    global ptrR
    print(ptrR-ptrL)

def empty(queue):
    global ptrL
    global ptrR
    if ptrL==ptrR: print(1)
    else: print(0)

def front(queue):
    global ptrL
    global ptrR
    if ptrL==ptrR: print(-1)
    else: print(queue[ptrL])

def back(queue):
    global ptrL
    global ptrR
    if ptrL==ptrR: print(-1)
    else: print(queue[ptrR-1])

for _ in range(n):
    cmd=sys.stdin.readline().split()

    if cmd[0] == 'push': push(queue, int(cmd[1]))
    elif cmd[0] == 'pop': pop(queue)
    elif cmd[0] == 'size': size(queue)
    elif cmd[0] == 'empty': empty(queue)
    elif cmd[0] == 'front': front(queue)
    elif cmd[0] == 'back': back(queue)
    