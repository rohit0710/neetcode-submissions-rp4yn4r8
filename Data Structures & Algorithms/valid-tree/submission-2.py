class Union_find:
    def __init__(self, n):
        self.group = [id for id in range(n)]
        self.rank = [0 for _ in range(n)]
    def find(self, edge):
        if self.group[edge] != edge:
            self.group[edge] = self.find(self.group[edge])
        return self.group[edge]
    
    def union(self, u, v):
        groupu = self.find(u)
        groupv = self.find(v)

        if groupu == groupv:
            return False

        if self.rank[groupv] > self.rank[groupu]:
            self.group[groupu] = groupv
            self.rank[groupv] += 1
        else:
            self.group[groupv] = groupu
            self.rank[groupu] += 1

        return True

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        uf = Union_find(n)
        for u, v in edges:
            if uf.union(u,v):
                n -= 1
            else:
                return False
        
        return n == 1