N= int(input())

def getHansuCount(num):
    if num<=99: return print(num)
    
    elif num>=100:
        cnt=99
        for i in range(100, num+1):
            i100=i//100
            i10=i//10-i100*10
            i1=i%10
            if i10*2==i100+i1: cnt+=1
        return print(cnt)
        
getHansuCount(N)

