class Solution {
    fun orangesRotting(grid: Array<IntArray>): Int {
        val m = grid.size
        val n = grid[0].size
        var fresh = 0
        val pq = ArrayDeque<Triple<Int, Int, Int>>()
        for (i in 0 until m)
            for (j in 0 until n)
                if (grid[i][j] == 1)
                    fresh ++
                else if(grid[i][j] == 2)
                    pq.add(Triple(i,j,0))

        if (fresh == 0)
            return 0
        var res = 0
        while(pq.isNotEmpty())
        {
            val (i,j, time) = pq.removeFirst()
            res = time
            if (i-1 in 0..m-1 && grid[i-1][j] == 1)
            {
                grid[i-1][j] = 2
                fresh --
                pq.add(Triple(i-1, j, time +1))
            }
            if (i+1 in 0..m-1 && grid[i+1][j] == 1)
            {
                grid[i+1][j] = 2
                fresh --
                pq.add(Triple(i+1, j, time +1))
            }
            if (j-1 in 0..n-1 && grid[i][j-1] == 1)
            {
                grid[i][j-1] = 2
                fresh--
                pq.add(Triple(i, j-1, time +1))
            }
            if (j+1 in 0..n-1 && grid[i][j+1] == 1)
            {
                grid[i][j+1] = 2
                fresh--
                pq.add(Triple(i, j+1, time +1))
            }
        }
        return if(fresh ==0) res else -1
    }
}
