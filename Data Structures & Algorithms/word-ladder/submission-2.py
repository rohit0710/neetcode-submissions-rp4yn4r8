class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if len(beginWord) != len(endWord) or endWord not in wordList:
            return 0

        dictionary = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                dictionary[word[:i]+ "*" + word[i+1:]].append(word)

        print(dictionary)
        self.count = 0
        visited= set()
        queue = deque()
        queue.append((beginWord, 1))

        while queue:
            word, level = queue.popleft()

            if word == endWord:
                return level

            for i in range(len(word)):
                for comb in dictionary[word[:i]+ "*" + word[i+1:]]:
                    if comb not in visited:
                        visited.add(comb)
                        queue.append((comb, level + 1))


        # def dfs(word, step):
        #     print(word)
        #     if word == endWord:
        #         self.count = min(self.count, step + 1)
        #
        #     for i in range(len(word)):
        #         for comb in dictionary[word[:i]+ "*" + word[i+1:]]:
        #             if comb not in visited:
        #                 visited.add(comb)
        #                 dfs(comb, step + 1)
        #
        # dfs(beginWord, 0)
        return self.count
