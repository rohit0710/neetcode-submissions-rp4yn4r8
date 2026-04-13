class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isPalindrome(i,j):
            while i >=0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            return [j - i + 1, i +1, j]
        
        maxl = [0,0,0]
        for i in range(len(s)):
            even = isPalindrome(i, i+1)
            odd = isPalindrome(i, i)

            maxl = max(maxl, even, odd, key = lambda x: x[0])

        return s[maxl[1]: maxl[2]]