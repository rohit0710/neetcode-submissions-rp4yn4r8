class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s)+1, len(p)+1
        memo = [[False] * n for _ in range(m)]
        memo[0][0] = True

        for j in range(1, n):
            if p[j-1] == "*":
                memo[0][j] = memo[0][j-2]
        
        for i in range(1, m):
            for j in range(1, n):
                if p[j-1] in {".", s[i-1]}:
                    memo[i][j] = memo[i-1][j-1]
                else:
                    if p[j-1] == "*":
                        memo[i][j] = memo[i][j-2]
                        if p[j-2] in {".", s[i-1]}:
                            memo[i][j] = memo[i][j] or memo[i-1][j]
        return memo[-1][-1]