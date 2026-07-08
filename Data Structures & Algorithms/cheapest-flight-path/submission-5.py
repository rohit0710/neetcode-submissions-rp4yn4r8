class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)

        for fro, to, price in flights:
            graph[fro].append((to, price))
        
        heap = []
        heapq.heappush(heap, (0, 0, src, [src]))

        map = dict()

        while heap:
            cost, stops, city, path = heapq.heappop(heap)

            if city == dst:
                return cost
            
            if stops > k:
                continue
            
            for nei, fare in graph[city]:
                ncost = cost + fare
                if (nei, stops+1) not in map or map[(nei, stops+1)] > ncost:
                    map[(nei, stops+1)] = ncost
                    heapq.heappush(heap, (ncost, stops+1, nei, path + [nei]))
        
        return -1