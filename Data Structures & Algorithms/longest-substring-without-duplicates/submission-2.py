class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map = dict()
        l, ans = 0,0
        for i in range(len(s)):
            if s[i] in map:
                l = max(l, map[s[i]])
            ans = max(ans, i - l + 1)
            map[s[i]] = i + 1
        return ans