import sys

sys.stdin=open('input.txt', 'r')
sys.stdout=open('output.txt', 'w')


n, m = map(int, input().split())

visit=[0 for _ in range(n+1)]

for i in sys.stdin.read().split():
    visit[int(i)]=1


# print(visit)

# step=1
# state=1

result=0

def jump(step, state, cnt):
    global n
    global visit
    global result
    state+=step
    cnt+=1
    if visit[state]==1:
        return

    if state>=n:
        if result==0:
            result=(state,cnt)
        elif result!=0:
            if result[1]>cnt:
                result=(state, cnt)

    if state+step<=n:
        jump(step, state, cnt)
    if state+step+1<=n:
        jump(step+1,state,cnt)
    if step>1 and state+step-1<=n:
        jump(step-1,state,cnt)

jump(1, 1, 0)

print(result[1])


