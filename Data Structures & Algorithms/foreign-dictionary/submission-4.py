class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = {x: [] for word in words for x in word}

        for i in range(1, len(words)):
            first = words[i-1]
            second = words[i]
            minl = len(min(first, second, key = len))
            if first[:minl] == second[:minl] and len(first) > len(second):
                return ""
            for k in range(minl):
                if first[k] != second[k]:
                    graph[first[k]].append(second[k])
                    break
        
        print(graph)

        res = []
        visited= set()
        completed = set()

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
        
        for x in graph.keys():
            if x not in completed:
                if not dfs(x):
                    return ""

        return "".join(res[::-1])
