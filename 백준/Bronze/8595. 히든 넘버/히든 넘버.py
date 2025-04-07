import sys

input=sys.stdin.readline

n=input()
strr=input()

for i in range(0, 26):
    chrr1=chr(i+65)
    strr=strr.replace(chrr1, ' ')
    chrr2=chr(i+97)
    strr=strr.replace(chrr2, ' ')

print(sum(map(int, strr.split())))