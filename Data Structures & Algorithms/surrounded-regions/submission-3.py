class Solution:
    def solve(self, grid: List[List[str]]) -> None:
        dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        m, n = len(grid), len(grid[0])
        def dfs(i, j):
            grid[i][j] = "S"
            for d in dir:
                ni, nj = i + d[0], j + d[1]
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == "O":
                    dfs(ni, nj)
        

        for i in range(m):
            if grid[i][0] == "O":
                dfs(i, 0)
            if grid[i][n-1] == "O":
                dfs(i, n-1)
        for j in range(n):
            if grid[0][j] == "O":
                dfs(0, j)
            if grid[m-1][j] == "O":
                dfs(m-1, j)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "O":
                    grid[i][j] = "X"
                if grid[i][j] == "S":
                    grid[i][j] = "O"