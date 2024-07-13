class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)
        lIdx = 0
        minLength = 10**9 
        sum_ = 0

        for rIdx in range(n):
            sum_ += nums[rIdx]
            while sum_ >= target:
                minLength = min(minLength, rIdx - lIdx + 1)
                if minLength == 1:
                    return 1
                sum_ -= nums[lIdx]
                lIdx += 1
        
        return minLength if minLength!=10**9 else 0