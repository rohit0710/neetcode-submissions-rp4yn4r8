class Solution {
    fun minEatingSpeed(piles: IntArray, h: Int): Int {
        if(piles.size == h)
            return piles.max()
        var low = 1
        var high = piles.max()
        var k = 0
        while(low <= high)
        {
            val mid = (low+high)/2
            var tempEatingRate = 0.0
            for (p in piles)
                tempEatingRate += ceil((p.toDouble() / mid))
            
            if(tempEatingRate <= h)
            {
                k = mid
                high = mid - 1
            }
            else
                low = mid + 1
        }
        return k
    }
}
