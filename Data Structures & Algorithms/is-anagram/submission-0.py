class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        char_set_s = [0] * 26
        char_set_t = [0] * 26
        for ch in s:
            char_set_s[ord(ch) - ord('a')] += 1
        
        for ch in t:
            char_set_t[ord(ch) - ord('a')] += 1
        
        return char_set_s == char_set_t

