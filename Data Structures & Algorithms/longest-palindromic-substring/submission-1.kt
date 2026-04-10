class Solution {
    fun longestPalindrome(s: String): String {
        
        fun palindrome(i: Int, j: Int): Triple<Int, Int, Int> {
            var i = i
            var j = j
            while (i >= 0 && j < s.length && s[i] == s[j]) {
                i--
                j++
            }
            return Triple(j-i+1, i+1, j)
        }
        var res = Triple(0,0,0)
        for (i in s.indices) {
            var even = palindrome(i, i)
            var odd = palindrome(i, i+1)
            var lmax = maxOf(even, odd, compareBy {it.first})
            res = maxOf(res, lmax, compareBy {it.first})
        }
        return s.substring(res.second, res.third)

    }
}
