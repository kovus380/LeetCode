class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def dfs(x, y):
            if x < 0 or x >= len(grid2) or y < 0 or y >= len(grid2[0]) or grid2[x][y] == 0:
                return
            
            grid2[x][y] = 0
            

            dfs(x - 1, y)
            dfs(x + 1, y)
            dfs(x, y - 1)
            dfs(x, y + 1)
            
        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                if grid2[i][j] == 1 and grid1[i][j] == 0:
                    dfs(i, j)
                    
        answer = 0
        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                if grid2[i][j] == 1:
                    dfs(i, j)
                    answer += 1
                    
        return answer