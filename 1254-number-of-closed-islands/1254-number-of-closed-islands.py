class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        def dfs(x, y):
            if (x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0])) or grid[x][y] == 1:
                return
            
            grid[x][y] = 1
                
            dfs(x - 1, y)
            dfs(x + 1, y)
            dfs(x, y - 1)
            dfs(x, y + 1)
            
            
        def dfs_side(x, y):
            if (x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0])) or grid[x][y] == 1:
                return
            
            grid[x][y] = 1
                
            dfs(x - 1, y)
            dfs(x + 1, y)
            dfs(x, y - 1)
            dfs(x, y + 1)
                
            
        for i in range(len(grid)):
            if grid[i][0] == 0:
                dfs_side(i, 0)
            if grid[i][-1] == 0:
                dfs_side(i, len(grid[0]) - 1)
        
        
        for j in range(len(grid[0])):
            if grid[0][j] == 0:
                dfs_side(0, j)
            if grid[-1][j] == 0:
                dfs_side(len(grid) - 1, j)
                
        answer = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    dfs(i, j)
                    answer += 1
        return answer
        