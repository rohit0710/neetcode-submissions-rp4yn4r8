class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        m,n = len(s1) +1, len(s2) +1

        memo = [[False for _ in range(n)] for _ in range(m)]
        memo[0][0] = True

        for i in range(1, m):
            memo [i][0] = memo[i-1][0] and s1[i-1] == s3[i-1]

        for i in range(1, n):
            memo[0][i] = memo[0][i - 1] and s2[i - 1] == s3[i - 1]

        for i in range(1, m):
            for j in range(1, n):
                memo[i][j] = memo[i-1][j] and s1[i-1] == s3[i + j -1] or memo[i][j - 1] and s2[j - 1] == s3[i +j - 1]

        return memo[-1][-1]