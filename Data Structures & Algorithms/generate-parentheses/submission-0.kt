class Solution {
    fun generateParenthesis(n: Int): List<String> {
        val res = mutableListOf<String>()
        fun helper(temp: String, open: Int, close: Int){
            if (temp.length == 2*n)
                res.add(temp)

            if (open < n)
                helper(temp + "(", open+1, close)

            if(close<open)
                helper(temp+")", open, close+1)
            
        }
        helper("", 0, 0)
        return res
    }
}
