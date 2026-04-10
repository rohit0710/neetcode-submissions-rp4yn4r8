class Solution {
    fun lastStoneWeight(stones: IntArray): Int {
        val pq = PriorityQueue<Int>()
        for (n in stones)
            pq.add(-n)

        while (pq.size > 1){
            val first = -pq.poll()
            val second = -pq.poll()

            val diff = abs(first - second)
            if (diff != 0)
                pq.add(-diff)
        }
        return if(pq.size == 1) -pq.peek() else 0
    }
}
