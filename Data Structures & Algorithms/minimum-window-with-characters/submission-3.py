class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window = defaultdict(int)
        res, l = [-1, -1], 0
        countT = Counter(t)
        have, need = 0, len(countT)
        reslen = float('inf')
        
        for r, ch in enumerate(s):
            window[ch] += 1
            if ch in countT and window[ch] == countT[ch]:
                have += 1

            while have == need:
                if reslen > r - l + 1:
                    res = [l, r]
                    reslen = r-l + 1

                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1

                l += 1

        return s[res[0]: res[1]+1] if reslen != float('inf') else ""
        