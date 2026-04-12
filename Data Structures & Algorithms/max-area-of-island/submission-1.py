class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        m,n = len(grid), len(grid[0])
        def count(i,j, ):
            if not 0<= i < m or not 0 <= j < n or grid[i][j] != 1:
                return 0
            
            grid[i][j] = 0
            self.area += 1
            count(i+1,j)
            count(i,j-1)
            count(i,j+1)
            count(i-1,j)
            
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    self.area = 0
                    count(i,j)
                    res = max(self.area, res)
        return res