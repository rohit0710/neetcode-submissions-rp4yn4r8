class Union_find:
    def __init__(self, n):
        self.group = [i for i in range(n)]
        self.rank = [0] * n
  
    def find(self, root):
        if self.group[root] != root:
            self.group[root] = self.find(self.group[root])
        return self.group[root]

    def union(self, roota, rootb):
        groupa = self.find(roota)
        groupb = self.find(rootb)

        if groupa == groupb:
            return False
        
        if self.rank[groupa] > self.rank[groupb]:
            self.rank[groupa] += 1
            self.group[groupb] = groupa
        else:
            self.rank[groupb] += 1
            self.group[groupa] = groupb
        return True

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        heap = []
        for i, (x1, y1) in enumerate(points):
            for j, (x2, y2) in enumerate(points):
                if i != j:
                    dist = abs(x1 - x2) + abs(y1 - y2)
                    heapq.heappush(heap, (dist, i, j))

        uf = Union_find(len(points))
        res = 0
        while heap:
            dist, i, j = heapq.heappop(heap)

            if uf.union(i, j):
                res += dist
        
        return res
