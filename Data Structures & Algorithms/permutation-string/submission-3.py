class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        if len(s2) < len(s1):
            return False
        m, n = len(s1), len(s2)
        ref = [0] * 26
        have = [0] * 26

        for i in range(m):
            ref[ord(s1[i]) - ord('a')] += 1
            have[ord(s2[i]) - ord('a')] += 1
        
        if ref == have:
            return True
        
        l = 0

        for r in range(m, n):
            have[ord(s2[r]) - ord('a')] += 1
            have[ord(s2[l]) - ord('a')] -= 1
            if have == ref:
                return True
            
            l += 1
        
        return False