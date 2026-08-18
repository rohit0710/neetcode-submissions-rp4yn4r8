class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)

        for fro,to,price in flights:
            graph[fro].append((price, to))

        
        heap = []
        heapq.heappush(heap, (0, 0, src))
        cost_map = {}
        while heap:
            price, stops, city = heapq.heappop(heap)

            if city == dst:
                return price
            
            if stops > k:
                continue

            for fare, new_city in graph[city]:
                new_price = price + fare
                if (new_city, stops+1) not in cost_map or cost_map[(new_city, stops+1)] > new_price:
                    cost_map[(new_city, stops+1)] = new_price
                    heapq.heappush(heap, (new_price, stops+1, new_city))
        
        return -1