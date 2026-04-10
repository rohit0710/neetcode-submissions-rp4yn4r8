class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for c, p in prerequisites:
            graph[c].append(p)

        self.is_poss = True
        visited = set()
        completed = set()

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
            return self.is_poss

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True