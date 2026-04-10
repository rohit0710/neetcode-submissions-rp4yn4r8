class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = [False] * (len(s) + 1)
        memo[0] = True

        for i in range(1, len(memo)+1):
            for word in wordDict:
                if s[i-1: i - 1 + len(word)] == word and memo[i - 1]:
                   memo[i+len(word)-1] = True
        return memo[-1]
