class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        n=len(numbers)
        
        # if numbers[0]+numbers[-1]==target:return [1,n]
        
        for i in range(n):
            lidx=i
            ridx=n-1
            temp=n-1
            
            while lidx<ridx:    
                # print(lidx, ridx)
                twosum=numbers[lidx]+numbers[ridx]
                if twosum>target:
                    temp=ridx
                    ridx=(lidx+ridx)//2
                elif twosum<target:
                    ridx=(ridx+temp+1)//2
                    if ridx==temp: break
                else: 
                    return [lidx+1, ridx+1]
                
                