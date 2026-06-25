class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        time = {x: float('inf') for x in range(1, n+1)}

        for u,v, t in times:
            graph[u].append((v, t))

        def bfs(root):
            que = deque()
            que.append((root, 0))
            while que:
                root, t = que.popleft()

                for nei, delta in graph[root]:
                    if nei not in time or time[nei] > t + delta:
                        time[nei] = t + delta
                        que.append((nei, t + delta))
        time[k] = 0
        bfs(k)
        
        print(time)
             
        return -1 if max(time.values()) == float('inf') else max(time.values())