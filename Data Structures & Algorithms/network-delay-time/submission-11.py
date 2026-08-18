class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u,v,t in times:
            graph[u].append((v, t))

        time_delay = {i: float('inf') for i in range(1,n+1)}
        time_delay[k] = 0
        que = deque()
        que.append((0, k))

        while que:
            t, node = que.popleft()

            for nei,time in graph[node]:
                if time_delay[nei] > time + t:
                    time_delay[nei] = time + t
                    que.append((time + t, nei))
        
        return max(time_delay.values()) if max(time_delay.values()) != float('inf') else -1