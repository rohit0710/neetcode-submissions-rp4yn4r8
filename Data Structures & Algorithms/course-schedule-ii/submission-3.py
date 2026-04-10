class Solution:
    def findOrder(self, numCourses: int, prereq: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for c, p in prereq:
            graph[c].append(p)

        visited = set()
        completed = set()
        res = []
        self.is_poss = True

        def dfs(root):
            if not self.is_poss:
                return False
            
            visited.add(root)
            
            for nei in graph[root]:
                if nei in visited:
                    self.is_poss = False
                    return False
                if nei not in completed:
                    dfs(nei)
                    
            visited.remove(root)
            completed.add(root)
            
            res.append(root)
            return self.is_poss
        
        for i in range(numCourses):
            if i not in completed:
                if not dfs(i):
                    return []
        
        return res