class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for fro, to in tickets:
            heapq.heappush(graph[fro], to)
        path = []
        def dfs(root):
            while graph[root]:
                city = heapq.heappop(graph[root])
                dfs(city)
            path.append(root)

        dfs("JFK")
        return path[::-1]
