class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_graph = defaultdict(list)
        is_poss = True
        for cou, pre  in prerequisites:
            adj_graph[cou].append(pre)

        print(adj_graph)

        visited = set()
        completed = set()
        def dfs(root):
            nonlocal is_poss
            if not is_poss:
                return

            visited.add(root)
            for v in adj_graph[root]:
                if v in visited:
                    is_poss = False
                if v not in completed:
                    dfs(v)

            visited.remove(root)
            completed.add(root)
            return is_poss


        for node in range(numCourses):
            if not dfs(node):
                return False
        return True