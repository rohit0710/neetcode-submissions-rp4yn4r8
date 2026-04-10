class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind(len(edges))
        for u,v in edges:
            if not uf.union(u,v):
                return [u,v]
        return []

    pass

class UnionFind:
    def __init__(self, n):
        self.group = [id for id in range(n+1)]
        self.rank = [0] * (n+1)

    def find(self, person):
        if self.group[person] != person:
            self.group[person] = self.find(self.group[person])
        return self.group[person]

    def union(self, pA, pB):
        groupA = self.find(pA)
        groupB = self.find(pB)

        if groupB == groupA:
            return False

        if self.rank[groupA] > self.rank[groupB]:
            self.group[groupB] = groupA
            self.rank[groupA] += 1
        else:
            self.group[groupA] = groupB
            self.rank[groupB] += 1

        return True