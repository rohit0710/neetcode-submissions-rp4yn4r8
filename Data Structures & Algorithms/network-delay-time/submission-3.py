class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for u,v,t in times:
           graph[u].append((v,t))

        cost_map = {id+1: float('inf') for id in range(n)}

        def dfs(node, time):
            if cost_map[node] <= time:
                return
            cost_map[node] = time
            for nei, t in graph[node]:
                dfs(nei, t+time)

        dfs(k, 0)
        return max(cost_map.values()) if float('inf') not in cost_map.values() else -1