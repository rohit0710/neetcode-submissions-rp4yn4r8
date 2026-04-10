class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = dict()
        res, l = 0, 0
        for i, v in enumerate(s):
            if v in char_map:
                ind = char_map[v]
                l = max(l, ind)
            res= max(res, i - l + 1)
            char_map[v] = i + 1
        return res
