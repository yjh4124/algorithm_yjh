class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        
        rows, cols=len(grid), len(grid[0])
        start=[-1,-1]
        empty_cells=0
        
        def mark_visited(i, j):
            grid[i][j]=-1
            
        def unmark_visited(i, j):
            grid[i][j]=0   
        
        def is_visited(i, j):
            return grid[i][j]==-1
        
      
        def initialize_grid():
            nonlocal empty_cells, start
            
            for i in range(rows):
                for j in range(cols):
                    if grid[i][j]==1:
                        start=[i, j]
                    if grid[i][j]!=-1:
                        empty_cells+=1
                        
        def dfs_paths(x, y, visited_cnt):
            
            if grid[x][y] == 2:
                return visited_cnt == empty_cells
            
            path_cnt=0
            mark_visited(x, y)
            
            # up, right, down, left
            directions=[(-1,0), (0,1), (1, 0), (0, -1)]
            
            for dx, dy in directions:
                nx, ny= x+dx, y+dy
                if 0 <= nx < rows and 0 <= ny < cols and not is_visited(nx, ny):
                    path_cnt+=dfs_paths(nx, ny, visited_cnt+1)
            
            unmark_visited(x, y)
            
            return path_cnt
        
        initialize_grid()
        
        return dfs_paths(start[0], start[1], 1)
        
            