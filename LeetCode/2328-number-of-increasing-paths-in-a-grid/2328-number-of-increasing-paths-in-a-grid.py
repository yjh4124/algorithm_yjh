class Solution(object):
    def countPaths(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        m, n = len(grid), len(grid[0])
        memo_path = [[0] * n for _ in range(m)]
        mod = 10**9 + 7
        
        def _dfs(i, j):
            if memo_path[i][j] != 0:
                return memo_path[i][j]
            
            current_value = grid[i][j]
            total_paths = 1 
            
            directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] > current_value:
                    total_paths += _dfs(ni, nj)
                    
            memo_path[i][j] = total_paths % mod  
            return memo_path[i][j]
        
        # Start search from each element in the m*n grid.
        total = 0
        for i in range(m):
            for j in range(n):
                total += _dfs(i, j)
                
        total %= mod  
        return total
