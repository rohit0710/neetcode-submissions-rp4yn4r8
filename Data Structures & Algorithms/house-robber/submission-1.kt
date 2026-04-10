class Solution {
    fun rob(cost: IntArray): Int {
        if (cost.size == 1)
            return cost[0]
        if (cost.size == 2)
            return cost.max()
        var h0 =0
        var h1 = 0
        for (x in 0 until cost.size)
        {
            var temp = h1
            h1 = max(h1, h0 + cost[x])
            h0 = temp
        }
        return h1
    }
}
