from collections import deque

def getMakeTargetNum(numbers, target):
    numMakeTarget=0
    n=len(numbers)
    # memo=set((numbers[0], 0), (-numbers[0], 0))
    calcList=deque([(numbers[0], 0), (-numbers[0], 0)])
    
    while calcList:
        num, idx=calcList.popleft()
        idx+=1
        calc1=num+numbers[idx]
        calc2=num-numbers[idx]
        if idx<=n-2:
            calcList.append((calc1, idx))
            calcList.append((calc2, idx))
        elif idx==n-1:
            if calc1==target: numMakeTarget+=1
            if calc2==target: numMakeTarget+=1
    
    return numMakeTarget

def solution(numbers, target):
    answer = getMakeTargetNum(numbers, target)
    print(answer)
    return answer