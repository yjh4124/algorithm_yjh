import sys

d1, d2=map(int, input().split())

seats=dict()

for rad in range(d1, d2+1):
    for idx in range(rad):
        seats[rad/(idx+1)]=1

print(len((list(seats.values()))))