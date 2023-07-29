a, b, c= map(int, input().split())

def getMod(a, b):
    if b==1: return a%c
    else:
        partMod=getMod(a,b//2)
        if b%2==0: return (partMod*partMod)%c
        elif b%2==1: return (partMod*partMod*a)%c

print(getMod(a,b))
