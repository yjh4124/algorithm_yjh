import sys

t=int(input())

for _ in range(t):
    n=int(input())

    score=[]
    for _ in range(n):
        score.append(tuple(map(int, sys.stdin.readline().split())))

    score.sort(key=lambda x: (x[0],x[1]))
    # print(score)

    ppl=[score[0]]
    check=score[0][1]
    for a, b in score:
        if b<check:
            ppl.append((a, b))
            check=b

    print(len(ppl))