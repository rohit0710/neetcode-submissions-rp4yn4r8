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
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set()
        def dfs(root):
            if root in visited: return 

            visited.add(root)

            for nei in graph[root]:
                dfs(nei)
            
        count = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1

        return count