import sys
n=int(input())

meeting=[]
for _ in range(n):
    meeting.append(tuple(map(int, sys.stdin.readline().split())))

meeting.sort(key=lambda x: (x[1], x[0]))

# for i in range(0, n//2):
#     print(meeting[i], end=' ')
# print()
# for i in range(n//2,n):
#     print(meeting[i], end=' ')
# print()

next=0
plan=[]

for start, end in meeting:
    if start>=next and end>=next:
        plan.append((start, end))
        next=end

# print(plan)
print(len(plan))
