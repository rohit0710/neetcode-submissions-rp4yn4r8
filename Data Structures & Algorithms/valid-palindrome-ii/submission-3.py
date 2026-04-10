class Solution:
    def validPalindrome(self, s: str) -> bool:
        i,j = 0, len(s)-1
        already_deleted = False
        def isPalindrome(i,j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1
            if s[i].lower() == s[j].lower():
                i += 1
                j -= 1
            else: return isPalindrome(i+1, j) or isPalindrome(i, j-1)
        return True