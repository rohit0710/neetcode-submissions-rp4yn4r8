class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = [False for _ in range(len(s) + 1)]
        memo[0] = True
        for i in range(1, len(s)+1):
            for w in wordDict:
                if memo[i-1] and w == s[i-1: i-1 + len(w)]:
                    memo[i -1 + len(w)] = True

        return memo[-1]
