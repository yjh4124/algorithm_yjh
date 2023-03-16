from collections import deque

ppap_str = input()

# print(ppap_str)

ppap_que=deque(ppap_str)

stack=[]

check=0
precheck='A'

for i in ppap_str:
    
    if i=='P':
        stack.append(i)

    elif i=='A':
        if precheck=='A':
            print('NP')
            check=1
            
            break
    
        elif precheck=='P':
            if len(stack)!=0:
                stack.pop()

                if len(stack)!=0:
                    stack.pop()

                elif len(stack)==0:
                    print('NP')
                    check=1
                    
                    break
    precheck=i
    ppap_que.popleft()
    # print(stack, ppap_que)

# print(len(ppap_str))
if check==0: 
    if stack:
        if len(stack)==1:
            if precheck=='P':
                print('PPAP')
            elif precheck=='A':
                print('NP')
        elif len(stack)>1:
            print('NP')
            
    else: 
        print('NP')