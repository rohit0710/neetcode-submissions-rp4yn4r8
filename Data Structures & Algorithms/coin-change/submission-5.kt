class Solution {
    fun coinChange(coins: IntArray, amount: Int): Int {
        val dp = IntArray(amount + 1) {amount + 1}
        dp[0] = 0

        for (a in 0 until (amount +1))
            for (c in coins)
                if ((a-c) >= 0){
                    dp[a] = minOf(dp[a], dp[a-c]+1)
                }
        return if (dp.last() != (amount + 1)) dp.last() else -1
    }
}
