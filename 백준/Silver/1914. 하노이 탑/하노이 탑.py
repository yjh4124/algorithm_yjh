n=int(input())

def move(no, x, y):
    if no>1:
        move(no-1, x, 6-x-y)

    print(f'{x} {y}')

    if no>1:
        move(no-1, 6-x-y, y)

print(f'{pow(2,n)-1}')

if n<=20:
    move(n, 1, 3)