n=int(input())

def move(no, x, y, cnt):
    if no>1:
        move(no-1, x, 6-x-y,cnt)
        cnt+=1

    
    print(f'{x} {y}')

    if no>1:
        move(no-1, 6-x-y, y,cnt)

print(f'{pow(2,n)-1}')

if n<=20:
    move(n, 1, 3, 0)