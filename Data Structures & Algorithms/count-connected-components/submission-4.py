class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
        res = 0
        def dfs(root):
            visited.add(root)
            for chold in graph[root]:
                if chold not in visited:
                    dfs(chold)
        
        for i in range(n):
            if i not in visited:
                dfs(i)
                res += 1
        
        return res
