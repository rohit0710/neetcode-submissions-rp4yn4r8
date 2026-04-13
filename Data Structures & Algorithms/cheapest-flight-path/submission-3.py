class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for fro, to, fare in flights:
            graph[fro].append((fare, to))
        
        heap = [(0, 0, src)]
        city_fare = dict()

        while heap:
            cost, stops, city = heapq.heappop(heap)
            
            if city == dst:
                return cost

            if stops > k:
                continue
            
            for fare, next_city in graph[city]:
                new_cost = cost + fare

                if (next_city, stops+1) not in city_fare or city_fare[(next_city, stops+1)] > new_cost:
                    city_fare[(next_city, stops+1)] = new_cost
                    heapq.heappush(heap, (new_cost, stops+1, next_city))
        return -1