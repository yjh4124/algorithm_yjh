import sys

from collections import deque

n=int(input())

k=int(input())

apple=[list(map(int, input().split())) for i in range(k)]

l=int(input())

comm=deque([input().split() for i in range(l)])

# print(apple)
# print(comm)

dir=['up','right','down','left']
dir_num=1

pos={'s0':{'dir':dir[dir_num], 'x': 1, 'y': 1}}

# up: [-, 0], right: [0, +], down: [+, 0], left: [0, -]

t=0

check=comm.popleft()
check_t=int(check[0])
check_dir=check[1]

checkout=1
check_ls=[]
while checkout:
    # print('/////////')
        
    if (1<=pos['s0']['x']<=n and 1<=pos['s0']['y']<=n):
            
        # print(t, check_t)
        # print(pos)
        

        if [pos['s0']['x'],pos['s0']['y']] in check_ls:
            checkout=0
            break
        
        check_ls=[]
        for i in range(len(pos)):
            name_print='s'+str(i)

            check_ls.append([pos[name_print]['x'], pos[name_print]['y']])
            
        # print(check_ls)

        if [pos['s0']['x'],pos['s0']['y']] in apple:
            
            apple.remove([pos['s0']['x'],pos['s0']['y']])
            # print(f'-------------apple pop')
            # print(len(pos))


            name_new='s'+str(len(pos))
            name_tail='s'+str(len(pos)-1)
            pos[name_new]={'dir':pos[name_tail]['dir'], 'x': pos[name_tail]['x'], 'y': pos[name_tail]['y']}
        
        temp2=pos['s0']
        for i in range(len(pos)-1):
            name_temp='s'+str(i+1)
            name_pre='s'+str(i)
            temp=temp2
            temp2=pos[name_temp]
            pos[name_temp]=temp.copy()

        if t==check_t:
            if check_dir=='D':
                if dir_num!=3:
                    dir_num+=1
                    pos['s0']['dir']=dir[dir_num]
                elif dir_num==3:
                    dir_num=0
                    pos['s0']['dir']=dir[dir_num]
            elif check_dir=='L':
                if dir_num!=0:
                    dir_num-=1
                    pos['s0']['dir']=dir[dir_num]
                elif dir_num==0:
                    dir_num=3
                    pos['s0']['dir']=dir[dir_num]
            if len(comm)!=0:
                check=comm.popleft()
                check_t=int(check[0])
                check_dir=check[1]
        
        
        if pos['s0']['dir']=='up':
            # if i==0: 
            pos['s0']['x']-=1
            t+=1
            # continue
        elif pos['s0']['dir']=='right':
            # if i==0: 
            pos['s0']['y']+=1
            t+=1
            # continue
        elif pos['s0']['dir']=='down':
            # if i==0: 
            pos['s0']['x']+=1
            t+=1
            # continue
        elif pos['s0']['dir']=='left':
            # if i==0:     
            pos['s0']['y']-=1
            t+=1
            # continue
        

    else: checkout=0


print(t)

