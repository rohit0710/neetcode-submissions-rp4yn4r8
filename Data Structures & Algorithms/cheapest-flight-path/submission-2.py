class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph =  defaultdict(list)
        for s,d,f in flights:
            graph[s].append((d,f))
        
        heap = [(0,src, 0, [src])]
        stop_city_map = {}
        
        while heap:
            cost, city, stops, route = heapq.heappop(heap)
            
            if city == dst:
                return cost
            
            if stops > k:
                continue
            for dest, fare in graph[city]:
                new_cost = cost + fare
                if (dest, stops+1) not in stop_city_map or stop_city_map[(dest, stops+1)] > new_cost:
                    stop_city_map[(dest, stops + 1)] = new_cost
                    heapq.heappush(heap,(new_cost, dest, stops + 1, route+[src]) )
                    
        return -1