class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or len(beginWord) != len(endWord):
            return 0

        graph = defaultdict(list)

        for word in wordList:
            for i,ch in enumerate(word):
                wc_word = word[:i] + "*" + word[i+1:]
                graph[wc_word].append(word)

        que = deque()
        que.append((beginWord, 1))
        visited = set()
        while que:
            word, length = que.popleft()

            if word == endWord:
                return length
            
            visited.add(word)

            for i,ch in enumerate(word):
                wc_word = word[:i] + "*" + word[i+1:]
                for nei in graph[wc_word]:
                    if nei not in visited:
                        que.append((nei, length + 1))
        
        return 0
