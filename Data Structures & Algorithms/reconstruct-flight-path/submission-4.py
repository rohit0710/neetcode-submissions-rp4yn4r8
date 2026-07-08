class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)

        for fro, to in tickets:
            heapq.heappush(graph[fro], to)

        res = []
        def dfs(root):
            while graph[root]:
                dfs(heapq.heappop(graph[root]))
            res.append(root)
        
        dfs("JFK")
        return res[::-1]