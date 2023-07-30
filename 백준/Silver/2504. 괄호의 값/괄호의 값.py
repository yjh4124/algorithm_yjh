ps=input()
# print(ps)

stack=[]
cntx=0
cnty=0
result=0
precheck=''

for i in ps:
    
    if (cntx==-1) | (cnty==-1):
        print(0)
        break

    if i=='(':
        cntx+=1
        precheck='('
    elif i=='[':
        cnty+=1
        precheck='['
    elif i==')':
        if (precheck=='('):
            tempx=pow(2,cntx)
            tempy=pow(3,cnty)
            result+=tempx*tempy
            # print(result)
        if (precheck=='['):
            print(0)
            break
        precheck=')'
        cntx-=1
    elif i==']':
        if (precheck=='['):
            tempx=pow(2,cntx)
            tempy=pow(3,cnty)
            result+=tempx*tempy
            # print(result)
        if (precheck=='('):
            print(0)
            break
        precheck=']'
        cnty-=1
else: 
    if (cntx==0) & (cnty==0):
        print(result)
    else: print(0)