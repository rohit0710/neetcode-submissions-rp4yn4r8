class Solution {
    fun isInterleave(s1: String, s2: String, s3: String): Boolean {
        if (s1.length + s2.length != s3.length)
            return false

        val m = s1.length + 1
        val n = s2.length + 1
        val grid = Array(m) { BooleanArray(n) {false} }
        grid[0][0] = true

        for (i in 1 until m)
            grid[i][0] = grid[i-1][0] && s1[i-1] == s3[i-1]

        for (i in 1 until n)
            grid[0][i] = grid[0][i-1] && s2[i-1] == s3[i-1]

        for (i in 1 until m)
            for (j in 1 until n)
                grid[i][j] = (grid[i-1][j] && s1[i-1] == s3[i+j-1]) || (grid[i][j-1] && s2[j-1] == s3[i+j-1])
        
        return grid[m-1][n-1]
    }
}
