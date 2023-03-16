import sys

n=int(sys.stdin.readline())

ls=sorted(int(sys.stdin.readline()) for i in range(n))

for i in ls:
    print(i)