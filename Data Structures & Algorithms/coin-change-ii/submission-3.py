class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        dp = [[0]*(amount+1) for _ in range(len(coins)+1)]
        n = len(coins)

        for i in range(n + 1):
            dp[i][0] = 1
        
        for i in range(n-1, -1, -1):
            for a in range(1, amount+1):
                if a-coins[i] >= 0:
                    dp[i][a] = dp[i+1][a] + dp[i][a - coins[i]]
        
        return dp[0][-1]

