class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)
        counter_s1 = Counter(s1)
        i, j = 0, 0
        freq = defaultdict(int)
        if len(s1) > len(s2):
            return False

        if m == n:
            return counter_s1 == Counter(s2)

        print(counter_s1)
        for i in range(n):
            freq[s2[i]] += 1

            if i - j + 1 > m:
                freq[s2[j]] -= 1
                if freq[s2[j]] == 0:
                    del freq[s2[j]]
                j += 1

            if i - j + 1 == m and freq == counter_s1:
                return True

        return False
