import sys

s, n=input().split()

# print(list(n))

s=int(s)

for row in range(1, 2*s+4):
    for num in list(n):
        if num=="1":
            if row==1:print(*([' ' for _ in range(s+2)]+[' ']), sep='', end='')
            if 1<row<s+2: print(*([' ' for _ in range(s+1)]+['|']+[' ']), sep='', end='')
            if row==s+2: print(*([' ' for _ in range(s+2)]+[' ']), sep='', end='')
            if s+2<row<2*s+3: print(*([' ' for _ in range(s+1)]+['|']+[' ']), sep='', end='')
            if row==2*s+3: print(*([' ' for _ in range(s+2)]+[' ']), sep='', end='')

        elif num=="2":
            if row==1: print(*([' ']+['-' for _ in range(s)]+[' ']+[' ']), sep='', end='')
            if 1<row<s+2: print(*([' ' for _ in range(s+1)]+['|']+[' ']), sep='', end='')
            if row==s+2: print(*([' ']+['-' for _ in range(s)]+[' ']+[' ']), sep='', end='')
            if s+2<row<2*s+3: print(*(['|']+[' ' for _ in range(1)]+[' ' for _ in range(s)]+[' ']), sep='', end='')
            if row==2*s+3: print(*([' ']+['-' for _ in range(s)]+[' ']+[' ']), sep='', end='')
        
        elif num=="3":
            if row==1: print(*([' ']+['-' for _ in range(s)]+[' ']+[' ']), sep='', end='')
            if 1<row<s+2: print(*([' ' for _ in range(s+1)]+['|']+[' ']), sep='', end='')
            if row==s+2: print(*([' ']+['-' for _ in range(s)]+[' ']+[' ']), sep='', end='')
            if s+2<row<2*s+3: print(*([' ' for _ in range(s+1)]+['|']+[' ']), sep='', end='')
            if row==2*s+3: print(*([' ']+['-' for _ in range(s)]+[' ']+[' ']), sep='', end='')
        
        elif num=="4":
            if row==1: print(*([' ' for _ in range(s+2)]+[' ']), sep='', end='')
            if 1<row<s+2: print(*(['|']+[' ' for _ in range(s)]+['|']+[' ']), sep='', end='')
            if row==s+2: print(*([' ']+['-' for _ in range(s)]+[' ']+[' ']), sep='', end='')
            if s+2<row<2*s+3: print(*([' ' for _ in range(s+1)]+['|']+[' ']), sep='', end='')
            if row==2*s+3: print(*([' ' for _ in range(s+2)]+[' ']), sep='', end='')
        
        elif num=="5":
            if row==1: print(*([' ']+['-' for _ in range(s)]+[' ']+[' ']), sep='', end='')
            if 1<row<s+2: print(*(['|']+[' ' for _ in range(1)]+[' ' for _ in range(s)]+[' ']), sep='', end='')
            if row==s+2: print(*([' ']+['-' for _ in range(s)]+[' ']+[' ']), sep='', end='')
            if s+2<row<2*s+3: print(*([' ' for _ in range(s+1)]+['|']+[' ']), sep='', end='')
            if row==2*s+3: print(*([' ']+['-' for _ in range(s)]+[' ']+[' ']), sep='', end='')
        
        elif num=="6":
            if row==1: print(*([' ']+['-' for _ in range(s)]+[' ']+[' ']), sep='', end='')
            if 1<row<s+2: print(*(['|']+[' ' for _ in range(1)]+[' ' for _ in range(s)]+[' ']), sep='', end='')
            if row==s+2: print(*([' ']+['-' for _ in range(s)]+[' ']+[' ']), sep='', end='')
            if s+2<row<2*s+3: print(*(['|']+[' ' for _ in range(s)]+['|']+[' ']), sep='', end='')
            if row==2*s+3: print(*([' ']+['-' for _ in range(s)]+[' ']+[' ']), sep='', end='')
        
        elif num=="7":
            if row==1: print(*([' ']+['-' for _ in range(s)]+[' ']+[' ']), sep='', end='')
            if 1<row<s+2: print(*([' ' for _ in range(s+1)]+['|']+[' ']), sep='', end='')
            if row==s+2: print(*([' ' for _ in range(s+2)]+[' ']), sep='', end='')
            if s+2<row<2*s+3: print(*([' ' for _ in range(s+1)]+['|']+[' ']), sep='', end='')
            if row==2*s+3: print(*([' ' for _ in range(s+2)]+[' ']), sep='', end='')
        
        elif num=="8":
            if row==1: print(*([' ']+['-' for _ in range(s)]+[' ']+[' ']), sep='', end='')
            if 1<row<s+2: print(*(['|']+[' ' for _ in range(s)]+['|']+[' ']), sep='', end='')
            if row==s+2: print(*([' ']+['-' for _ in range(s)]+[' ']+[' ']), sep='', end='')
            if s+2<row<2*s+3: print(*(['|']+[' ' for _ in range(s)]+['|']+[' ']), sep='', end='')
            if row==2*s+3: print(*([' ']+['-' for _ in range(s)]+[' ']+[' ']), sep='', end='')
        
        elif num=="9":
            if row==1: print(*([' ']+['-' for _ in range(s)]+[' ']+[' ']), sep='', end='')
            if 1<row<s+2: print(*(['|']+[' ' for _ in range(s)]+['|']+[' ']), sep='', end='')
            if row==s+2: print(*([' ']+['-' for _ in range(s)]+[' ']+[' ']), sep='', end='')
            if s+2<row<2*s+3: print(*([' ' for _ in range(s+1)]+['|']+[' ']), sep='', end='')
            if row==2*s+3: print(*([' ']+['-' for _ in range(s)]+[' ']+[' ']), sep='', end='')
        
        elif num=="0":
            if row==1: print(*([' ']+['-' for _ in range(s)]+[' ']+[' ']), sep='', end='')
            if 1<row<s+2: print(*(['|']+[' ' for _ in range(s)]+['|']+[' ']), sep='', end='')
            if row==s+2: print(*([' ' for _ in range(s+2)]+[' ']), sep='', end='')
            if s+2<row<2*s+3: print(*(['|']+[' ' for _ in range(s)]+['|']+[' ']), sep='', end='')
            if row==2*s+3: print(*([' ']+['-' for _ in range(s)]+[' ']+[' ']), sep='', end='')
        
    print()       
    





    
