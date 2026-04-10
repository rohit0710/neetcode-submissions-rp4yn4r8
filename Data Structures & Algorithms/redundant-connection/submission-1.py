class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind(len(edges))
        for u,v in edges:
            if not uf.union(u,v):
                return [u,v]

        return []

class UnionFind:
    def __init__(self, n):
       self.group = [id for id in range(n+1)]
       self.rank = [0] * (n+1)

    def find(self, vertex):
        if self.group[vertex] != vertex:
            self.group[vertex] = self.find(self.group[vertex])
        return self.group[vertex]

    def union(self, vertexU, vertexV):
        groupU = self.find(vertexU)
        groupV = self.find(vertexV)

        if groupU == groupV:
            return False

        if self.rank[groupU] > self.rank[groupV]:
            self.group[groupV] = groupU
            self.rank[groupU] += 1
        else:
            self.group[groupU] = groupV
            self.rank[groupV] += 1

        return True
