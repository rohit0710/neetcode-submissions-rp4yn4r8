class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
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

        uf = Union_find(len(edges))

        for u,v in edges:
            if not uf.union(u,v):
                return [u,v]

        return []