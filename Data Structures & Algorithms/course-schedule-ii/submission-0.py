class Solution:
    def findOrder(self, numCourses: int, prereq: List[List[int]]) -> List[int]:
        adj_graph = defaultdict(list)
        visited = set()
        completed = set()
        res = []
        self.is_poss = True
        for c, p in prereq:
            adj_graph[c].append(p)

        def dfs(root):
            if not self.is_poss:
                return

            visited.add(root)
            for nei in adj_graph[root]:
                if nei in visited:
                    self.is_poss = False
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
