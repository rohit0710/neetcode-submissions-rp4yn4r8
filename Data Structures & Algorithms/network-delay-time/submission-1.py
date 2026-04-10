class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, t in times:
            graph[u].append((v, t))

        time_map = {i+1:float('inf') for i in range(n)}

        def dfs(u, t):
            if time_map[u] <= t:
                return
            time_map[u] = t
            for nei, ti in graph[u]:
                dfs(nei, t + ti)

        dfs(k, 0)
        res = max(time_map.values())
        return res if res != float('inf') else -1