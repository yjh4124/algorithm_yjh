class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        
        rows, cols=len(grid), len(grid[0])
        visited=[[0]*cols for _ in range(rows)]
        start=[-1,-1]
        empty_cells=0
        path_cnt=0
        
        def count_visited():
            return sum(sum(row) for row in visited)
        
        def mark_visited(i, j):
            visited[i][j]=1
            
        def unmark_visited(i, j):
            visited[i][j]=0   
        
        def is_visited(i, j):
            return visited[i][j]
        
      
        def initialize_grid():
            nonlocal empty_cells, start
            
            for i in range(rows):
                for j in range(cols):
                    if grid[i][j]==1:
                        start=[i, j]
                        mark_visited(i, j)
                        empty_cells+=1
                    elif grid[i][j]==0:
                        empty_cells+=1
                        
        def dfs_paths(x, y):
            nonlocal path_cnt
            
            # up, right, down, left
            directions=[(-1,0), (0,1), (1, 0), (0, -1)]
            
            for dx, dy in directions:
                nx, ny= x+dx, y+dy
                if 0 <= nx < rows and 0 <= ny < cols:
                    if grid[nx][ny] == 0 and not is_visited(nx, ny):
                        mark_visited(nx, ny)
                        dfs_paths(nx, ny)
                        unmark_visited(nx, ny)
                    elif grid[nx][ny] == 2 and count_visited() == empty_cells:
                        path_cnt += 1
                
        initialize_grid()
        dfs_paths(start[0], start[1])
        
        return path_cnt
        
            