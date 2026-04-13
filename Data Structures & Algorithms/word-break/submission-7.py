class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = [False for _ in range(len(s)+1)]
        memo[0] = True

        for i in range(1, len(memo)):
            for word in wordDict:
                if memo[i-1] and s[i-1: i +len(word)-1] == word:
                    memo[i+len(word)-1] = True

        return memo[-1]