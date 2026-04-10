class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if len(beginWord) != len(endWord) or endWord not in wordList:
            return 0
        wild_map = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                wild_card = word[:i] + "*" + word[i+1:]
                wild_map[wild_card].append(word)

        print(wild_map)
        que = deque()
        que.append((beginWord, 1))
        visited = set()

        while que:
            word, level = que.popleft()

            if word == endWord:
                return level

            visited.add(word)
            for i in range(len(word)):
                wild_card = word[:i] + "*" + word[i + 1:]
                for nei in wild_map[wild_card]:
                    if nei not in visited:
                        que.append((nei, level+1))
        return 0
