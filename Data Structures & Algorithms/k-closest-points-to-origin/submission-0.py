class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x,y in points:
            heap.append([x*x + y*y, x,y])
        res = []
        heapq.heapify(heap)
        while k > 0:
            dist, x,y = heapq.heappop(heap)
            res.append((x,y))
            k -= 1

        return res