class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        graph = defaultdict(list)

        for f,t, p in flights:
            graph[f].append((t, p))

        que = [(0, 0, src, [src])]
        map = defaultdict(int)

        while que:
            cost, stops, city, route = heapq.heappop(que)

            if city == dst:
                return cost
            
            if stops > k:
                continue

            for nei, fare in graph[city]:
                ncost = cost + fare
                if  (stops+1, nei) not in map or map[(stops+1, nei)] > ncost:
                    map[(stops+1, nei)] = ncost
                    heapq.heappush(que, (ncost, stops+1, nei, route + [nei]))

        return -1