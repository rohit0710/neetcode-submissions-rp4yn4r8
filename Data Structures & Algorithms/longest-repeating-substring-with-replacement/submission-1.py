class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, maxF = 0, 0
        counter = defaultdict(int)
        res = 0
        
        for r in range(len(s)):
            counter[s[r]] += 1
            maxF = max(maxF, counter[s[r]])
                       
            while (r-l + 1 -maxF) >  k:
                counter[s[l]] -= 1
                l += 1 
            res = max(res, r-l+1)
        
        return res