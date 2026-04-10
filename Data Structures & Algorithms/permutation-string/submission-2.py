class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
           return False

        s1_freq = [0] * 26
        s2_freq = [0] * 26

        for ch in s1:
            s1_freq[ord(ch) - ord('a')] += 1
        k = len(s1)
        l = 0
        for r,ch in enumerate(s2):
            s2_freq[ord(ch) - ord('a')] += 1

            if(r-l+1) > k:
                s2_freq[ord(s2[l]) - ord('a')] -= 1
                l += 1

            if (r - l + 1) == k:
                if s1_freq == s2_freq:
                    return True

        return False
