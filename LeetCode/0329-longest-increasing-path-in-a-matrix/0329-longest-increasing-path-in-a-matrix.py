class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        
        self.m=len(matrix)
        self.n=len(matrix[0])
        
        self.matrix=matrix
        self.memo_path=[[0]*self.n for _ in range(self.m)]
        
        longest_path=0
        # Start search from each element on m*n matrix. 
        for i in range(self.m):
            for j in range(self.n):
                if not self.memo_path[i][j]:
                    self.memo_path[i][j]=self._dfs(i, j)
                    longest_path=max(longest_path, self.memo_path[i][j])
                    
        return longest_path
    
    # DFS
    def _dfs(self, row, col):
        if self.memo_path[row][col]:
            return self.memo_path[row][col]
        
        i, j=(row, col)
        current_value=self.matrix[i][j]
        
        max_path_length=1
        
        # up, right, down, left
        directions=[[-1, 0], [0, 1], [1, 0], [0, -1]]
        
        for di, dj in directions:
            ni=i+di
            nj=j+dj

            if 0<=ni<self.m and 0<=nj<self.n:
                next_value=self.matrix[ni][nj]
                
                if next_value>current_value:    
                    max_path_length=max(max_path_length, 1+self._dfs(ni, nj))
            
        self.memo_path[row][col]=max_path_length
        
        return max_path_length
        
        
