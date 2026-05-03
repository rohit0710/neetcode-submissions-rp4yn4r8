from functools import cache
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        for i in range(n-1, -1, -1):
            for j in range(i, n):
                dp[i][j] = s[i]== s[j] and (j-i <= 2 or dp[i+1][j-1])
        
        
        @cache
        def dfs(st):
            if st == n:
                return [[]]

            ans = []

            for end in range(st, n):
                if dp[st][end]:
                    for rest in dfs(end+1):
                        ans.append([s[st:end+1]]+rest)
            
            return ans
        return dfs(0)