class Solution {
    fun isValid(s: String): Boolean {
        val map = mapOf<Char, Char>(
            '}' to '{',
            ']' to '[',
            ')' to '('
        )
        val stack = mutableListOf<Char>()
        for (ch in s)
            if(!map.containsKey(ch))
              stack.add(ch)
            else
            {
                if (!stack.isEmpty() && stack.last() == map[ch])
                    stack.removeLast()
                else
                    return false
            }
        return if(stack.isEmpty()) true else false
    }
}
