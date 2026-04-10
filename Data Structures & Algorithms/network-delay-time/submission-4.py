class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u,v,t in times:
            graph[u].append((v,t))

        time_map = {x+1: float('inf') for x in range(n)}

        def dfs(root, time):
            if time_map[root] <= time:
                return
            time_map[root] = time
            for nei, t in graph[root]:
                dfs(nei, time + t)
        
        
        dfs(k, 0)
        return max(time_map.values()) if float('inf') not in time_map.values() else -1