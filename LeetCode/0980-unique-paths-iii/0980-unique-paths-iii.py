class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        
        m, n=len(grid), len(grid[0])
        visited=[[0]*n for _ in range(m)]
        location=[-1,-1]
        empty_cnt=0
        paths_cnt=0
        
        def visited_cnt():
            return sum(sum(row) for row in visited)
        
        def visited_on(i, j):
            visited[i][j]=1
            
        def visited_off(i, j):
            visited[i][j]=0   
        
        def is_visited(i, j):
            return visited[i][j]
        
      
        def initialize_grid_info():
            nonlocal empty_cnt
            nonlocal location
            
            for i in range(m):
                for j in range(n):
                    if grid[i][j]==1:
                        location=[i, j]
                        visited_on(i, j)
                        empty_cnt+=1
                    elif grid[i][j]==0:
                        empty_cnt+=1
                        
        def dfs_paths():
            nonlocal empty_cnt
            nonlocal paths_cnt
            nonlocal location
            
            # up, right, down, left
            directions=[(-1,0), (0,1), (1, 0), (0, -1)]
            
            for di, dj in directions:
                location[0]+=di
                location[1]+=dj
                i=location[0]
                j=location[1]
                if i<0 or i>=m or j<0 or j>=n: 
                    location[0]-=di
                    location[1]-=dj
                    continue
                    
                if grid[i][j]==0 and not is_visited(i, j):
                    visited_on(i, j)
                    dfs_paths()
                    visited_off(i, j)
                elif grid[i][j]==2 and visited_cnt()==empty_cnt:
                    paths_cnt+=1
                
                location[0]-=di
                location[1]-=dj
                
        initialize_grid_info()
        dfs_paths()
        
        return paths_cnt
        
            