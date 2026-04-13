class Solution:
    def countSubstrings(self, s: str) -> int:
        def isPalindrome(i,j):
            while i >=0 and j < len(s) and s[i] == s[j]:
                res.append(s[i:j+1])
                i -= 1
                j += 1
            return [j - i + 1, i +1, j]
        
        res = list()
        for i in range(len(s)):
            even = isPalindrome(i, i+1)
            odd = isPalindrome(i, i)

        return len(res)