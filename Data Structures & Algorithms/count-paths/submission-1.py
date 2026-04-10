class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[1 for x in range(n)] for _ in range(m)] 
        for i in range(1, m):
            memo [i][0] = 1 
        
        for i in range(1, n):
            memo [0][i] = 1 
            
        for i in range(1, m):
            for j in range(1, n):
                memo[i][j] = memo[i-1][j] + memo[i][j-1]

        return memo[-1][-1]