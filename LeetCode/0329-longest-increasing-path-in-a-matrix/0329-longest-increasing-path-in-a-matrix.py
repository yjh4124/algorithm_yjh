class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        self._initialize(matrix)
        
        longest_path=0
        
        # Start search from each element in m*n matrix. 
        for i in range(self.m):
            for j in range(self.n):
                if not self.memo_path[i][j]:
                    longest_path=max(longest_path, self._dfs(i, j))
                    
        return longest_path
    
    def _initialize(self, matrix):
        self.m=len(matrix)
        self.n=len(matrix[0])
        self.matrix=matrix
        self.memo_path=[[0]*self.n for _ in range(self.m)]
        
    def _dfs(self, i, j):
        if self.memo_path[i][j]:
            return self.memo_path[i][j]
        
        current_value=self.matrix[i][j]
        max_path_length=1
        
        # up, right, down, left
        directions=((-1, 0), (0, 1), (1, 0), (0, -1))
        
        for di, dj in directions:
            ni=i+di
            nj=j+dj

            if 0<=ni<self.m and 0<=nj<self.n:
                next_value=self.matrix[ni][nj]
                
                if next_value>current_value:    
                    max_path_length=max(max_path_length, 1+self._dfs(ni, nj))
            
        self.memo_path[i][j]=max_path_length
        
        return max_path_length
        
        
