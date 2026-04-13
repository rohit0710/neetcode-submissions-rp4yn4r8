class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = {c: [] for w in words for c in w}

        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            minl = min(len(w1), len(w2))

            if len(w1) > len(w2) and w1[:minl] == w2[:minl]:
                return ""
            for j in range(minl):
                if w1[j] != w2[j]:
                    graph[w1[j]].append(w2[j])
                    break
        print(graph)

        visited= set()
        completed = set()
        res = []

        def dfs(root):
            if root in visited:
                return False
            
            visited.add(root)
            for ch in graph[root]:
                if ch in visited:
                    return False
                if ch not in completed:
                    dfs(ch)

            visited.remove(root)
            completed.add(root)
            res.append(root)

            return True
        
        for c in graph:
            if c not in completed:
                if not dfs(c):
                    return ""

        
        return "".join(res[::-1])
            