class Solution:
    def networkDelayTime(self, vals: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        times = {x: float('inf') for x in range(1, n+1)}

        for u,v,t in vals:
            graph[u].append((v, t))
        
        que = deque()
        que.append((k, 0))
        times[k] = 0

        while que:
            root, t = que.popleft()
            for nei, time in graph[root]:
                if times[nei] > t + time:
                    times[nei] = t + time
                    que.append((nei, t + time))
        
        return -1 if max(times.values()) == float('inf') else max(times.values())
