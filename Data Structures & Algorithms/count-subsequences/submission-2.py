class Solution:
    def numDistinct(self, s: str, t: str) -> int:        
        m,n = len(s), len(t)
        if m < n:
            return 0
        
        memo= [[0]*(n+1) for _ in range(m+1)]

        for i in range(m+1):
            memo[i][0] = 1
        for i in range(1, m+1):
            for j in range(1, n+1):
                memo[i][j] = memo[i-1][j]
                if s[i-1] == t[j-1]:
                    memo[i][j] += memo[i-1][j-1]
        


        return memo[-1][-1]