class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)

        for fro, to in tickets:
            heapq.heappush(graph[fro], to)
        
        res = []
        print(graph)
        def dfs(dest):
            while graph[dest]:
                dfs(heapq.heappop(graph[dest]))
            res.append(dest)

        dfs("JFK")
        return res[::-1]