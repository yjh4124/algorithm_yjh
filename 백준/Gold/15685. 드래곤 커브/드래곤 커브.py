import sys

n=int(input())

data=[[int(data) for data in sys.stdin.readline().split()] 
      for _ in range(n)]

# print(data)

dx=(0,-1,0,1)
dy=(1,0,-1,0)

size=101
graph=[[0 for _ in range(size)] for _ in range(size)]

for y, x, d, g in data:
    
    stack=[]
    stack.append((x,y))
    stack.append((x+dx[d],y+dy[d]))

    graph[x][y]=1
    graph[x+dx[d]][y+dy[d]]=1
    num_point=2
    # print(stack)

    for _ in range(g):
        # print(stack)
        pivot_x, pivot_y=stack[-1][0], stack[-1][1]
        # print(pivot_x, pivot_y)
        graph[pivot_x][pivot_y]=1
        
        for i in range(num_point-1):
            idx=num_point-2-i
            pre_x, pre_y=stack[idx][0], stack[idx][1]
            # graph[pre_x][pre_y]=1

            new_x=pivot_x+(pre_y-pivot_y)
            new_y=pivot_y-(pre_x-pivot_x)
            # print((pre_x, pre_y), (new_x, new_y))
            if 0<=new_x<=size-1 and 0<=new_y<=size-1:
                graph[new_x][new_y]=1
                stack.append((new_x, new_y))

        num_point=num_point*2-1
        


r,c=0,0
cnt=0
for col in range(size-1):
    for row in range(size-1):
        sum_=graph[row][col]+graph[row+1][col]\
            +graph[row][col+1]+graph[row+1][col+1]
        if sum_==4:
            cnt+=1
print(cnt)

        
        

