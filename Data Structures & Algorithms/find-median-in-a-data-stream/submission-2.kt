class MedianFinder() {
    val small = PriorityQueue<Int>() //Max-heap
    val big = PriorityQueue<Int>() //min-heap

    fun addNum(num: Int) {
        if(small.size == big.size)
        {
            big.add(num)
            val minV = -big.poll()
            small.add(minV)
        }
        else
        {
            small.add(-num)
            val maxV = -small.poll()
            big.add(maxV)
        }
    }

    fun findMedian(): Double {
        if(small.size == big.size)
            return (big.peek() - small.peek())/2.0
        else
            return (-small.peek())/1.0

    }

}
