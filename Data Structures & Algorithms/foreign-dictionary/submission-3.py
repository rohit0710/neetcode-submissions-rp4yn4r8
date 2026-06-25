class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = {x: [] for w in words for x in w}

        for i in range(1, len(words)):
            first = words[i-1]
            second = words[i]

            minl = len(min(first, second))

            if first[:minl] == second[:minl]:
                if len(first) > len(second):
                    return ""
            
            for i in range(minl):
                if first[i] != second[i]:
                    graph[first[i]].append(second[i])
                    break
        
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
        
        for x in  graph.keys():
            if x not in completed:
                if not dfs(x):
                    return ""
        
        return "".join(res[::-1])

