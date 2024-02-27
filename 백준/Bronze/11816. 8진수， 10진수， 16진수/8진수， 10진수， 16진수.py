import sys

input=sys.stdin.readline

x=input().strip()

lenn=len(x)
result=0
if x[0]=='0':
    if x[1]=='x':
        for i in range(lenn-1, 1, -1):
            if x[i] in [str(i) for i in range(0, 10)]: result+=int(x[i])*16**(lenn-1-i)
            else: 
                result+=(int(ord(x[i]))-87)*16**(lenn-1-i)
    else:
        for i in range(lenn-1, 0, -1):
            result+=int(x[i])*8**(lenn-1-i)
else:
    for i in range(lenn-1, -1, -1):
        result+=int(x[i])*10**(lenn-1-i)
        
print(result)