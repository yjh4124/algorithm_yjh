import sys
# sys.setrecursionlimit(10**8)
n, m=[int(i) for i in sys.stdin.readline().split()]

# print(n)
# print(m)

ls_tree=sorted([int(i) for i in input().split()], reverse=1)

# print(m)
# print(ls_tree)

          
def bi_cut(ls_tree,cut_h,pre_cut,temp):

    temp=0
    diff=(abs(cut_h-pre_cut+1)+1)//2
    # if diff==0: diff=1
        # cnt+=1
    up_cut=cut_h+diff
    down_cut=cut_h-diff
    for i in ls_tree:
        if i>cut_h:
            temp+=i-cut_h
                
    if ((cut_h==pre_cut)&(temp>m))|(temp==m):
        return print(cut_h)
    
    if temp>m: # 너무 낮게 자름
        # print(f'{cut_h}--{temp}')
        bi_cut(ls_tree, up_cut, cut_h,temp)
    else: # 너무 높게 자름
        # print(f'{cut_h}--{temp}')
        bi_cut(ls_tree, down_cut, cut_h,temp)

bi_cut(ls_tree,ls_tree[0]//2, ls_tree[0],0)
