class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        # def recurse(s, t):
        #     if len(t) == 0:
        #         return 1
            
        #     if len(s) == 0:
        #         return 0

        #     if s[0] == t[0]:
        #         return recurse(s[1:], t[1:]) + recurse(s[1:], t)
        #     else:
        #         return recurse(s[1:], t)
        # return recurse(s, t)
        
        m,n = len(s)+1, len(t)+1
        if m < n:
            return 0
        
        memo= [[0]*n for _ in range(m)]
        for i in range(m):
            memo[i][0] = 1
        for i in range(1,m):
            for j in range(1,n):
                memo[i][j] = memo[i-1][j]
                if s[i-1] == t[j-1]:
                    memo[i][j] += memo[i-1][j-1]

        return memo[-1][-1]

