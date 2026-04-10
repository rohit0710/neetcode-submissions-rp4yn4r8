class Solution {
    fun climbStairs(n: Int): Int {
        if (n == 1)
            return 1
        if (n == 2)
            return 2
        var h1=1
        var h2 = 2
        for(i in 2 until n){
            var temp = h2
            h2 = h1 + h2
            h1 = temp
        }
        return h2
    }
}
