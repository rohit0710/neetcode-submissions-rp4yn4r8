class KthLargest(k: Int, nums: IntArray) {

    val pq = PriorityQueue<Int>()
    val k = k
    init {
        for (n in nums){
            pq.add(n)
            if(pq.size > k)
                pq.poll()
        }
    }
    fun add(`val`: Int): Int {
        pq.add(`val`)
        if(pq.size > k)
            pq.poll()
        return pq.peek()
    }

}
