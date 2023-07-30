str_=input()

def checkValVPS(str_):
    stackVPS=[]
    total=0
    tempTotal=0
    temp=1

    for idx in range(len(str_)):
        char_=str_[idx]
        if char_=='(':
            temp*=2
            stackVPS.append(char_)
        elif char_==')':
            if str_[idx-1]=='(': tempTotal+=temp
            temp//=2
            if stackVPS and stackVPS[-1]=='(': stackVPS.pop()
            else: return print(0)
        elif char_=='[':
            temp*=3
            stackVPS.append(char_)
        elif char_==']':
            if str_[idx-1]=='[': tempTotal+=temp
            temp//=3
            if stackVPS and stackVPS[-1]=='[': stackVPS.pop()
            else: return print(0)

        if not stackVPS: total+=tempTotal; tempTotal=0

    if not stackVPS: return print(total)
    else: return print(0)

checkValVPS(str_)