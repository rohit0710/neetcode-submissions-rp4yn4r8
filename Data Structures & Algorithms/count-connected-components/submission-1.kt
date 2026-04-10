class Solution {
    fun countComponents(n: Int, edges: Array<IntArray>): Int {
        val graph = mutableMapOf<Int, MutableList<Int>>()
        for((u,v) in edges){
            graph.getOrPut(u){mutableListOf()}.add(v)
            graph.getOrPut(v){mutableListOf()}.add(u)
        }
        val visited = mutableSetOf<Int>()
        var res = 0
        fun dfs(root: Int){
            visited.add(root)
            for (nei in graph[root] ?: emptyList())
                if (!visited.contains(nei))
                    dfs(nei)
        }
        for (i in 0 until n)
            if (!visited.contains(i)){
                res++
                dfs(i)
            }
        return res
    }
}
