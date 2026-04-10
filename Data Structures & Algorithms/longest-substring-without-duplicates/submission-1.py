class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = dict()
        ans = 0
        l = 0
        for i, v in enumerate(s):
            if v in char_map:
                l = max(l, char_map[v])
            ans = max(ans, i - l + 1)
            char_map[v] = i + 1
        return ans