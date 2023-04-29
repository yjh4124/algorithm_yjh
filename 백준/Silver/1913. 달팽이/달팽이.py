import sys


n=int(input())

num=int(input())

# print(n, num)

snail_arr=[[0 for _ in range(n)] for _ in range(n)]

# for i in snail_arr:
#     print(i)

row, col=0, 0
cnt=n**2

dx=(1,0,-1,0)
dy=(0,1,0,-1)
idx=0

num_x, num_y=0,0

while (cnt!=0):
    if snail_arr[row][col]==0:
        snail_arr[row][col]=cnt
        if cnt==num:
            num_x=row+1
            num_y=col+1
        cnt-=1
    row+=dx[idx%4]
    col+=dy[idx%4]
    
    if (row<0 or row>n-1 or col<0 or col>n-1 or snail_arr[row][col]!=0):
        row-=dx[idx%4]
        col-=dy[idx%4]
        idx+=1

for i in snail_arr:
    print(*i)

print(num_x, num_y)