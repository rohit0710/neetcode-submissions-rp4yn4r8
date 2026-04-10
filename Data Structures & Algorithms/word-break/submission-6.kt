class Solution {
    fun wordBreak(s: String, wordDict: List<String>): Boolean {
        val memo = Array(s.length + 1) {false}
        memo[0] = true

        for (i in 1..s.length)
            for (w in wordDict)
                if(memo[i-1] && w == s.substring(i-1, minOf(i + w.length -1, s.length)))
                    memo[i + w.length -1] = true
        
        return memo.last()
    }
}
