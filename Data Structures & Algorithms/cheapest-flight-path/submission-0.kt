class Solution {
    fun findCheapestPrice(n: Int, flights: Array<IntArray>, src: Int, dst: Int, k: Int): Int {
        val graph: MutableMap<Int, MutableList<Pair<Int, Int>>> = mutableMapOf()
        for(flight in flights) {
            val (source, destination, fare) = flight
            graph.getOrPut(source){mutableListOf()}.add(Pair(destination, fare))
        }
        val pq = PriorityQueue<Triple<Int, Int, Int>>(compareBy { it.first })
        val cityStopMap= mutableMapOf<Pair<Int, Int>, Int>()
        pq.add(Triple(0, src, 0))

        while(pq.isNotEmpty()){
            val (cost, node, stops) = pq.poll()
            if (node == dst) return cost
            if (stops > k) continue
            for (nextPort in graph.getOrDefault(node, mutableListOf()))
            {
                val (neighbour, fare) = nextPort
                val newCost = cost + fare
                if(cityStopMap.getOrDefault(Pair(neighbour, stops+1), Int.MAX_VALUE) > newCost)
                {
                    cityStopMap[Pair(neighbour, stops+1)] = newCost
                    pq.add(Triple(newCost, neighbour, stops+1))
                }
            }
        }
        return -1
    }
}
