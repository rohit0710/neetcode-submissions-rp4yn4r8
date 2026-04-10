class UnionFind:
    def __init__(self, n):
        self.group = [i for i in range(n+1)]
        self.rank = [0] * (n+1)

    def find(self, a):
        if self.group[a] != a:
            self.group[a] = self.find(self.group[a])
        return self.group[a]

    def union(self, a, b):
        ga = self.find(a)
        gb = self.find(b)

        if ga == gb:
            return False

        if self.rank[ga] > self.rank[gb]:
            self.group[gb] = ga
            self.rank[ga] += 1
        else:
            self.group[ga] = gb
            self.rank[gb] += 1
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind(len(edges))
        for u,v in edges:
            if not uf.union(u,v):
                return [u,v]