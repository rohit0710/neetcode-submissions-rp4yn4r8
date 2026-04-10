class Solution:
    def minDistance(self, s1: str, s2: str) -> int:
        
        m,n = len(s1)+1, len(s2)+1

        memo = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(1, m):
            memo[i][0] = 1 + memo[i-1][0]
        for i in range(1, n):
            memo[0][i] = 1 + memo[0][i-1]
            
        for i in range(1, m):
            for j in range(1, n):
                if s1[i-1] == s2[j-1]:
                    memo[i][j] = memo[i-1][j-1]
                else:
                    memo[i][j] = 1 + min(memo[i-1][j-1], memo[i][j-1], memo[i-1][j])
        return memo[-1][-1]