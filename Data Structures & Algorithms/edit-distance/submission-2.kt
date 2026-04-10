class Solution {
    fun minDistance(word1: String, word2: String): Int {
        val m = word1.length + 1
        val n =  word2.length + 1
        
        val memo = Array(m) { IntArray(n) {0} }
        
        for (i in 1 until m)
            memo[i][0] = 1 + memo[i-1][0]

        for (i in 1 until n)
            memo[0][i] = 1 + memo[0][i-1]

        for (i in 1 until m)
            for (j in 1 until n)
                if (word1[i-1] == word2[j-1])
                    memo[i][j] = memo[i-1][j-1]
                else
                    memo[i][j] = minOf(memo[i-1][j-1], memo[i][j-1], memo[i-1][j]) +1
        
        return memo[m-1][n-1]
    }
}
