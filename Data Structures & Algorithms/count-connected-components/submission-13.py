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
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        uf = Union_find(n)
        count = n
        for u,v in edges:
            if uf.union(u,v):
                
                count -= 1
        
        return count 

        # graph = defaultdict(list)
        # for u,v in edges:
        #     graph[u].append(v)
        #     graph[v].append(u)
        
        # visited = set()
        # def dfs(root):
        #     if root in visited: return 

        #     visited.add(root)

        #     for nei in graph[root]:
        #         dfs(nei)
            
        # count = 0
        # for i in range(n):
        #     if i not in visited:
        #         dfs(i)
        #         count += 1

        # return count