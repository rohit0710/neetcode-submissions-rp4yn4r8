class Solution {
    fun minCostClimbingStairs(cost: IntArray): Int {
        if (cost.size == 1)
            return cost[0]
        if (cost.size == 2)
            return cost.min()
        var h0 =cost[0]
        var h1 = cost[1]
        for (x in 2 until cost.size)
        {
            var temp = h1
            h1 = min(h1, h0) + cost[x]
            h0 = temp
        }
        return min(h1, h0)
    }
}
