class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        coins.sort()
        memo = [[0] * (amount+1) for _ in range(n + 1)]
        for i in range(n+1):
            memo[i][0] = 1
        for i in range(n-1, -1, -1):
            for a in range(amount+1):
                if a-coins[i] >= 0:
                    memo[i][a] =memo[i+1][a]+memo[i][a - coins[i]]

        return memo[0][-1]