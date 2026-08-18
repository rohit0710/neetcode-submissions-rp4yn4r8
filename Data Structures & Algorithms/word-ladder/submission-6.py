class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        word_map = defaultdict(list)
        for word in wordList:
            for i, w in enumerate(word):
                wc = word[:i] + "*" + word[i+1:]
                word_map[wc].append(word)

        que = deque()
        que.append((beginWord, 1))
        visited = {beginWord}
        while que:
            word, dist = que.popleft()
            if word == endWord:
                return dist

            for i, w in enumerate(word):
                wc = word[:i] + "*" + word[i+1:]
                for nei in word_map[wc]:
                    if nei not in visited:
                        visited.add(nei)
                        que.append((nei, dist + 1))
        
        return 0

