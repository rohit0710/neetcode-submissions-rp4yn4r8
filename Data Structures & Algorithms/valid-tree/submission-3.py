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
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        uf = Union_find(n)
        count = n
        for u,v in edges:
            if not uf.union(u,v):
                return False
            count -= 1
        
        return count == 1