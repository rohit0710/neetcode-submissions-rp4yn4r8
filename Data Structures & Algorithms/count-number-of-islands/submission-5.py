class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        m,n = len(grid), len(grid[0])
        def count(i,j):
            if not 0<= i < m or not 0 <= j < n or grid[i][j] != "1":
                return
            
            grid[i][j] = "0"
            count(i+1,j)
            count(i,j-1)
            count(i,j+1)
            count(i-1,j)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    count(i,j)
                    res += 1
        return res
