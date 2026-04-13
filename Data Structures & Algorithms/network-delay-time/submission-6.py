class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for u,v,t in times:
            graph[u].append((v,t))

        node_time = {id:float('inf') for id in range(1, n+1)}

        def dfs(root, t):
            if node_time[root] <= t:
                return
            
            node_time[root] = t 

            for nei,time in graph[root]:
                dfs(nei, t + time)

        dfs(k, 0)
        return max(node_time.values()) if max(node_time.values()) != float('inf') else -1
