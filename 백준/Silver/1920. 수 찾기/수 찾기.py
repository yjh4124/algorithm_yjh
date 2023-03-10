n=int(input())

arr_n=sorted([int(i) for i in input().split()])

def bi_find(arr_n, m, start, end):
    # print(f'{arr_n} {start} {end}')
    if start!=end:
        if m == arr_n[(start+end)//2]:
            print(1)
            return
        elif m > arr_n[(start+end)//2]:
            bi_find(arr_n, m, (start+end+1)//2,end)
        elif m < arr_n[(start+end)//2]:
            bi_find(arr_n, m, start, (start+end-1)//2)
    
    elif start==end:
        if m == arr_n[(start+end)//2]:
            print(1)
        else:
            print(0)
        return

m=int(input())

arr_m=[bi_find(arr_n,int(j),0,len(arr_n)-1) for j in input().split()]