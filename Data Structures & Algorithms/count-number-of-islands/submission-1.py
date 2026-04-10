class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n = len(grid), len(grid[0])
        def dfs(i, j):
            if 0 <= i < m and 0 <= j < n and grid[i][j] != "0":
                grid[i][j] = "0"
                dfs(i+1, j) 
                dfs(i, j+1) 
                dfs(i, j-1) 
                dfs(i-1, j) 
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    dfs(i, j)
                    res += 1
        
        return res