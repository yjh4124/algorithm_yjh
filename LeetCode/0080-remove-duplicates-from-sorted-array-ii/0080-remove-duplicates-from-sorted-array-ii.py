class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt=1
        for idx, num in enumerate(nums):
                
            if idx+1<=len(nums)-1:
                if nums[idx]==nums[idx+1]:
                    cnt+=1
                else:
                    cnt=1
            
            if cnt==3:
                while idx+1<=len(nums)-1 and nums[idx]==nums[idx+1]:
                    nums.pop(idx)
                cnt=1
                