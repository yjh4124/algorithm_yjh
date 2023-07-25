T= int(input())

def makePrimeSet(num):
    primeNum={i for i in range(2,num+1)}

    for i in range(2, int(num**0.5)+1):
        cnt=0

        while (i*(i+cnt))<=num:
            if (i*(i+cnt)) in primeNum: primeNum.remove(i*(i+cnt))
            cnt+=1
    
    return primeNum

primeNum=makePrimeSet(10000)

def getGoldbachPartition(num):
    if num==4: return print(2, 2)
    
    startNum=num//2 if (num//2)%2==1 else num//2-1
    for i in range(startNum, 1, -2):
        if (i in primeNum) and (num-i in primeNum):
            return print(i, num-i)

for _ in range(0, T):
    getGoldbachPartition(int(input()))
