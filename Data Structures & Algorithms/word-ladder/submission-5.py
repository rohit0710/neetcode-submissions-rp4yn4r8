class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        graph = defaultdict(list)
        if endWord not in wordList:
            return 0
        
        for word in wordList:
            for i in range(len(word)):
                wc = word[:i] + "*" + word[i+1:]
                graph[wc].append(word)
        
        que = deque()
        que.append((beginWord, 1))
        visited = {beginWord}
        while que:
            word, dist = que.popleft()

            if word == endWord:
                return dist
            
            for i in range(len(word)):
                wc = word[:i] + "*" + word[i+1:]
                for nei in graph[wc]:
                    if nei not in visited:
                        visited.add(nei)
                        que.append((nei, dist + 1))
        
        return 0