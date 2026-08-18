class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for c, p in prerequisites:
            graph[c].append(p)

        visited = set()
        completed = set()
        res = []

        def dfs(root):
            if root in visited:
                return False
            
            visited.add(root)

            for nei in graph[root]:
                if nei in visited:
                    return False
                if nei not in completed:
                    dfs(nei)
            
            visited.remove(root)
            completed.add(root)
            res.append(root)

            return True
        
        for n in range(numCourses):
            if n not in completed:
                if not dfs(n):
                    return []
        
        return res