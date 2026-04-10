class Solution:
    def countSubstrings(self, s: str) -> int:
        p_substring = list()

        def isPalindrome(i, j):
            while i >= 0 and j < len(s) and s[i] == s[j]:
                p_substring.append(s[i: j])
                i -= 1
                j += 1

            return [j - i + 1, i + 1, j]

        for i in range(len(s)):
            s1 = isPalindrome(i, i)
            s2 = isPalindrome(i, i + 1)

        return len(p_substring)