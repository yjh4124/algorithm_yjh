class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(numbers)

        for i in range(n):
            lidx = i
            ridx = n - 1

            while lidx < ridx:
                twosum = numbers[lidx] + numbers[ridx]
                if twosum > target:
                    ridx -= 1
                elif twosum < target:
                    lidx += 1
                else:
                    return [lidx + 1, ridx + 1]
