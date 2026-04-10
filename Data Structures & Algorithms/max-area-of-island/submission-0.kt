class Solution {
    fun maxAreaOfIsland(grid: Array<IntArray>): Int {
        val m = grid.size
        val n = grid[0].size

        fun dfs(i: Int,j: Int): Int {
            if((i !in 0 until m ) || (j !in 0 until n) || grid[i][j] != 1)
                return 0 
            grid[i][j] = 0
            return (1 + dfs(i-1,j) + dfs(i+1,j) + dfs(i,j+1) + dfs(i,j-1))
        }
        var res = 0
        for(i in 0 until m)
            for (j in 0 until n)
                if (grid[i][j] == 1){
                    res = maxOf(res, dfs(i,j))
                }
        return res
    }
}
