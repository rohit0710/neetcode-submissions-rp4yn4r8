class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited = set()
        
        def dfs(root):
            if root in visited:
                return
            
            visited.add(root)
            
            for nei in graph[root]:
                if nei not in visited:
                    dfs(nei)
        
        count = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1
        
        return count
