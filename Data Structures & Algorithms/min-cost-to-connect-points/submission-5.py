class Union_find:
    def __init__(self, n):
        self.group = [id for id in range(n + 1)]
        self.rank = [0 for _ in range(n+1)]

    def find(self, edge):
        if self.group[edge] != edge:
            self.group[edge] = self.find(self.group[edge])
        return self.group[edge]
    
    def union(self, u, v):
        group_u = self.find(u)
        group_v = self.find(v)

        if group_u == group_v:
            return False

        if self.rank[group_u] > self.rank[group_v]:
            self.group[group_v]= group_u
            self.rank[group_u] += 1
        else:
            self.group[group_u]= group_v
            self.rank[group_v] += 1

        return True

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        heap = []

        for i in range(len(points)):
            for j in range(i+1, len(points)):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                heapq.heappush(heap, (dist, i, j))
        
        uf = Union_find(len(points))

        res = 0

        count = len(points)

        while count > 1 and heap:
            dist, i, j = heapq.heappop(heap)

            if uf.union(i, j):
                res += dist
                count -= 1
        
        return res
        
