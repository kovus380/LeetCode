class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(x, y, a):
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == 0:
                return 0
            
            grid[x][y] = 0
            a += 1
            
            return a + dfs(x + 1, y, 0) + dfs(x, y + 1, 0) + dfs(x - 1, y, 0) + dfs(x, y - 1, 0)
        
        
        areas = [0]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    area = dfs(i, j, 0)
                    print(area)
                    areas.append(area)
        return max(areas)
            
        