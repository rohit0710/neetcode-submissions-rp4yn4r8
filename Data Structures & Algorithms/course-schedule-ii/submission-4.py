class Solution:
    def findOrder(self, numCourses: int, prereq: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for c,p in prereq:
            graph[c].append(p)

        visited = set()
        completed = set()
        res = list()

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
        
        for i in range(numCourses):
            if i not in completed:
                if not dfs(i):
                    return []
        
        return res