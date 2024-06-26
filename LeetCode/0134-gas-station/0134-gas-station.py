class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        idx=0
        n=len(gas)
        
        if sum(gas)<sum(cost):
            return -1
        
        while idx<n:
            current=idx
            tank=gas[current]
            for _ in range(n):
                tank=tank-cost[current]
                current+=1
                current=current%n
                if tank<0:
                    idx=current
                    break
                tank+=gas[current]
                
            else:
                return idx
                break
             
        return -1
                