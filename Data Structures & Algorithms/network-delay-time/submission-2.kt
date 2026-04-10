class Solution {
    fun networkDelayTime(times: Array<IntArray>, n: Int, k: Int): Int {
        val graph = mutableMapOf<Int, MutableList<Pair<Int, Int>>>()
        for ((u,v,w) in times)
            graph.getOrPut(u) {mutableListOf()}.add(Pair(v, w))

        val timeCount = IntArray(n+1){Int.MAX_VALUE}
        timeCount[0] = 0
        fun dfs(root: Int, time: Int) {
            if(timeCount[root] < time)
                return

            timeCount[root] = time
            for ((nei, t) in graph[root] ?: emptyList())
                dfs(nei, time + t)
        }
        
        dfs(k, 0)
        return if (timeCount.max() == Int.MAX_VALUE) -1 else timeCount.max()

    }
}
