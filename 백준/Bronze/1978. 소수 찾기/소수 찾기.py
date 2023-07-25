N= int(input())
numSet=set(map(int, input().split()))

def makePrimeSet(num):
    primeNum={i for i in range(2,num+1)}

    for i in range(2, int(num**0.5)+1):
        cnt=0

        while (i*(i+cnt))<=num:
            if (i*(i+cnt)) in primeNum: primeNum.remove(i*(i+cnt))
            cnt+=1
    
    return primeNum

primeNum=makePrimeSet(1000)

def getPrimeCount(numSet):
    return print(len(primeNum & numSet))

getPrimeCount(numSet)
