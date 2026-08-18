class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for f, t in tickets:
            heapq.heappush(graph[f], t)

        res = []
        def dfs(city):
            while graph[city]:
                dfs(heapq.heappop(graph[city]))
            res.append(city)
        
        dfs("JFK")

        return res[::-1]