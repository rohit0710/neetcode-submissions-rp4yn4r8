class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        def dfs(i,j):
            if not 0<= i < m or not 0 <= j < n or grid[i][j] != 1:
                return 0

            grid[i][j] = 0
            res = 1+ dfs(i,j+1) + dfs(i,j-1) + dfs(i-1,j)+ dfs(i+1,j)

            return res 
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    count = dfs(i,j)
                    res = max(res, count)
        return res