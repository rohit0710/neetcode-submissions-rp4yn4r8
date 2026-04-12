class Solution:
    def solve(self, grid: List[List[str]]) -> None:
        dir = [(1,0), (-1,0), (0, 1), (0, -1)]
        m, n = len(grid), len(grid[0])
        def dfs(i,j):
            if not 0 <= i < m or not 0 <=j < n or grid[i][j] != "O":
                return
            
            grid[i][j] = "S"
            for d in dir:
                r,c = i + d[0], j + d[1]
                dfs(r,c)
        
        for i in range(m):
            dfs(i, 0)
            dfs(i, n-1)
        
        for i in range(n):
            dfs(0, i)
            dfs(m-1, i)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "O":
                    grid[i][j] = "X"
                if grid[i][j] == "S":
                    grid[i][j] = "O"