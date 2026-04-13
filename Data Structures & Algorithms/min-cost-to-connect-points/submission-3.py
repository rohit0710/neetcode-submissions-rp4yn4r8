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
        conns = []
        for i, (x1,y1) in enumerate(points):
            for j, (x2, y2) in enumerate(points):
                if i != j:
                    d = abs(x1-x2) + abs(y1-y2)
                    heapq.heappush(conns, (d, i, j))
        
        res = 0
        uf = Union_find(len(points))
        while conns:
            d, i, j = heapq.heappop(conns)

            if uf.union(i,j):
                res += d
        
        return res

                
        