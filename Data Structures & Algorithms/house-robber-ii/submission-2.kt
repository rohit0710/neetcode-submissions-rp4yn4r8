class Solution {
    fun rob(cost: IntArray): Int {
        fun simple(cost:IntArray): Int
        {   var h0 =0
            var h1: Int = 0
            for (x in 0 until cost.size)
            {
                var temp = h1
                h1 = maxOf(h1, h0 + cost[x])
                h0 = temp
            }
            return h1}
        if (cost.size == 1) return cost.first()
        return maxOf(simple(cost.dropLast(1).toIntArray()),simple( cost.drop(1).toIntArray()))

    }
}
