class Solution {
    fun numIslands(grid: Array<CharArray>): Int {
        val m = grid.size
        val n = grid[0].size
        fun dfs(i: Int, j: Int) {
            if (i in 0..m-1 && j in 0..n-1 && grid[i][j]== '1')
            {
                grid[i][j] = '0'
                dfs(i-1,j)
                dfs(i,j-1)
                dfs(i+1,j)
                dfs(i,j+1)
            }
        }
        var res= 0
        for (i in 0..m-1)
            for (j in 0 .. n-1)
                if (grid[i][j] == '1') {
                    dfs(i,j)
                    res++
                }
                
        return res
    }
}
