class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        m, n = len(matrix), len(matrix[0])
        memo_path = [[0] * n for _ in range(m)]
        longest_path = 0
        
        def _dfs(i, j):
            if memo_path[i][j]:
                return memo_path[i][j]
            
            current_value = matrix[i][j]
            max_path_length = 1
            
            directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] > current_value:
                    max_path_length = max(max_path_length, 1 + _dfs(ni, nj))
            
            memo_path[i][j] = max_path_length
            return max_path_length
        
        for i in range(m):
            for j in range(n):
                if not memo_path[i][j]:
                    longest_path = max(longest_path, _dfs(i, j))
                    
        return longest_path
