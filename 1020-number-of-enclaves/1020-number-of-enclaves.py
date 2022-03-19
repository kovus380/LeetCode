class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def dfs_boundary(x, y):
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == 0:
                return
            
            grid[x][y] = 0
            
            dfs_boundary(x - 1, y)
            dfs_boundary(x + 1, y)
            dfs_boundary(x, y - 1)
            dfs_boundary(x, y + 1)
            
        for i in range(len(grid)):
            dfs_boundary(i, 0)
            dfs_boundary(i, len(grid[0]) - 1)
            
        for j in range(len(grid[0])):
            dfs_boundary(0, j)
            dfs_boundary(len(grid) - 1, j)
        
        print(grid)
        answer = [s.count(1) for s in grid]
        return sum(answer)
        