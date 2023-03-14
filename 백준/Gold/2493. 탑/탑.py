import sys

n=int(sys.stdin.readline())

tower=[int(i) for i in sys.stdin.read().split()]

r_tower=[]
memo=[]

cnt=0
for i in range(n):
    while memo:
        if tower[i]<tower[memo[-1]]:
            print(memo[-1]+1,end=' ')
            memo.append(i)
            # print(f'2--{memo}, {not memo}')
            break
        elif tower[i]>tower[memo[-1]]:
            memo.pop()
            # print(f'3--{memo}, {not memo}')  
    if not memo:
        print(0, end=' ')
        memo.append(i)
        # print(f'1--{memo}, {not memo}')  