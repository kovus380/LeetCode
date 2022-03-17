class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        def dfs(x, y):
            if x < len(image) and x >= 0 and y < len(image[0]) and y >= 0:
                if image[x][y] == newColor:
                    return
                if image[x][y] == color:
                    image[x][y] = newColor
                    dfs(x + 1, y)
                    dfs(x - 1, y)
                    dfs(x, y + 1)
                    dfs(x, y - 1)
            return
        color = image[sr][sc]
        dfs(sr, sc)
        return image