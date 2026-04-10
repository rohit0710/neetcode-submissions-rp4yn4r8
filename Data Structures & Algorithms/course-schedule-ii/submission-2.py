class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for c, p in prerequisites:
            graph[c].append(p)

        self.is_poss = True
        visited = set()
        completed = set()
        self.res = []
        def dfs(u):
            if u in visited:
                return False

            visited.add(u)
            for nei in graph[u]:
                if nei in visited:
                    self.is_poss = False
                if nei not in completed:
                    dfs(nei)

            visited.remove(u)
            completed.add(u)
            self.res.append(u)
            return self.is_poss

        for i in range(numCourses):
            if i not in completed:
                if not dfs(i):
                    return []
        return self.res