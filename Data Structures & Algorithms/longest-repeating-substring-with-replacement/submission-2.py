class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i, maxf = 0, 0
        charmap = defaultdict(int)
        res = 0

        for j in range(len(s)):
            charmap[s[j]] += 1
            maxf = max(maxf, charmap[s[j]])

            while (j - i + 1 - maxf) > k:
                charmap[s[i]] -= 1
                i += 1
            
            res = max(res, j - i + 1)
        return res
                
