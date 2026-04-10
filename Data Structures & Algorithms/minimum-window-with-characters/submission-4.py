class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_counter = Counter(t)
        s_counter = defaultdict(int)
        need = set(t_counter.keys())
        have = set()
        l = 0
        res_len = float('inf')
        res = []
        for r in range(len(s)):
            if s[r] in t_counter:
                s_counter[s[r]] += 1
                if s_counter[s[r]] >= t_counter[s[r]]:
                    have.add(s[r])

            while have == need:
                if res_len > (r - l + 1):
                    res_len = r - l + 1
                    res = [l, r+1]
                if s[l] in t_counter and s[l] in s_counter:
                    s_counter[s[l]] -= 1
                    if s_counter[s[l]] < t_counter[s[l]]:
                        have.remove(s[l])

                l += 1

        return s[res[0] : res[1]] if res_len != float('inf') else ""
