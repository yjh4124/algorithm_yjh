import sys

input = sys.stdin.readline

n = int(input())

def getPrime(number):
    
    primes=[1]*(number+1)
    primes[0]=0
    primes[1]=0
    
    for i in range(2, int(number**0.5)+1):
        if primes[i]==0:
            j=i
            while i*j<=number:
                primes[i*j]=0
                j+=1
    
    return primes

primeList=getPrime(n)

for i in range(1, n+1):
    if primeList[i]==1:
        while n%i==0:
            print(i)
            n//=i
        
        
    