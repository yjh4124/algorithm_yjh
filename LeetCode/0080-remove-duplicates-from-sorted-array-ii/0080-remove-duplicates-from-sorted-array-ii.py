class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 1
        tmp = 0
        while i < len(nums):
            if nums[i - 1] == nums[i]:
                if tmp == 1:
                    nums.pop(i)
                    i -= 1
                else:
                    tmp += 1
            else:
                tmp = 0
            i += 1
        return len(nums)
        