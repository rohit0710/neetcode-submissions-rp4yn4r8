class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for fro,to,cost in flights:
            graph[fro].append((to, cost))

        min_stop_cost_city_map = dict()
        heap = [(0, 0, src, [src])]

        while heap:
            cost, stops, city, route= heapq.heappop(heap)
            
            if city == dst:
                return cost

            if stops > k:
                continue
                
            for nextCity, fare in graph[city]:
                new_cost = cost+fare
                if (nextCity, stops+1) not in min_stop_cost_city_map or min_stop_cost_city_map[(nextCity, stops+1)] > new_cost:
                    min_stop_cost_city_map[(nextCity, stops + 1)] = new_cost
                    heapq.heappush(heap, (new_cost, stops+1, nextCity, route+[nextCity]))
        return -1