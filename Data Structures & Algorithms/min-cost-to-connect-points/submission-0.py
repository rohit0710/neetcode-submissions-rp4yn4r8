class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        dist = []

        for i, (x,y) in enumerate(points):
            for j, (a,b) in enumerate(points[i+1:], start = i+1):
                d = abs(x-a) + abs(y-b)
                dist.append((d, i, j))

        dist.sort()
        uf = UnionFind(len(points))
        res = 0
        for dis,u, v  in dist:
            if uf.union(u,v):
                res += dis

        return res

class UnionFind:
    def __init__(self, n):
        self.group = [id for id in range(n+1)]
        self.rank = [0] * (n+1)

    def find(self, point):
        if self.group[point] != point:
            self.group[point] = self.find(self.group[point])
        return self.group[point]

    def union(self, pointA, pointB):
        groupA = self.find(pointA)
        groupB = self.find(pointB)

        if groupA == groupB:
            return False

        if self.rank[groupA] > self.rank[groupB]:
            self.rank[groupA] += 1
            self.group[groupB] = groupA
        else:
            self.rank[groupB] += 1
            self.group[groupA] = groupB

        return True