import sys

eq=input()

eq='0'+eq

data=[]
numls=[]
idx=0

num=''
for ea in eq:
    if ea!='+' and ea!='-':
        num+=ea
    elif ea=='+' or ea=='-':
        data.append((idx-1,int(num)))
        num=''
        if ea =='+':
            data.append((idx,'+'))
        if ea =='-':
            data.append((idx,'-'))
    idx+=1
data.append((idx-1,int(num)))

# print(numls)
# print(data)

result=0
check=1

for i in range(len(data)):
    idx=data[i][0]
    value=data[i][1]

    if value!='+' and value!='-':
        if check==1:
            result+=value
        elif check==-1:
            result-=value
    elif value=='-':
        if check==1:
            check*=-1
        elif check!=1:
            continue
    elif value=='+':
        continue
        
print(result)