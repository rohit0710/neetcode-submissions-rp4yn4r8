class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        dist = []

        for i, (x1, y1) in enumerate(points):
            for j, (x2, y2) in enumerate(points[i+1:], start= i+1):
                d = abs(x2-x1) + abs(y2-y1)
                dist.append((d,i,j))

        dist.sort()
        uf = UnionFind(len(points))
        res = 0
        for dis, u, v in dist:
            if uf.union(u,v):
                res += dis

        return res

    pass

class UnionFind:
    def __init__(self, n):
        self.group = [id for id in range(n)]
        self.rank = [0] * n
        
    def find(self, edge):
        if self.group[edge] != edge:
            self.group[edge] = self.find(self.group[edge])
        return self.group[edge]
    
    def union(self, u, v):
        gu = self.find(u)
        gv = self.find(v)
        
        if gu == gv:
            return False
        
        if self.rank[gu] < self.rank[gv]:
            self.group[gu] = gv
            self.rank[gv] += 1
        else:
            self.group[gv] = gu
            self.rank[gu] += 1
        
        return True