class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited = set()
        count = 0
        
        def dfs(root):            
            visited.add(root)
            for nei in graph[root]:
                if nei not in visited:
                    dfs(nei)
                    
        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1
        
        return count