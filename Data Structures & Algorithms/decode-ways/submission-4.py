class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        dp = [0] * (n+1)

        if s[0] == "0":
            return 0
        
        dp[0] = 1
        for i in range(1, n+1):
            if s[i-1] != "0":
                dp[i] = dp[i-1]
            if i >= 2 and ((s[i-2] == "2" and s[i-1] in "0123456") or s[i-2] == "1"):
                    dp[i] += dp[i-2]
        
        return dp[-1]
