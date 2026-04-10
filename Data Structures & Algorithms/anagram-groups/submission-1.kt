class Solution {
    fun groupAnagrams(strs: Array<String>): List<List<String>> {
        val word_list = mutableMapOf<List<Int>, MutableList<String>>()

        for (str in strs)
        {
            val charList = MutableList<Int>(26) {0}
            for(c in str.lowercase())
            {
                charList[c - 'a']++
            }

            word_list.getOrPut(charList) { mutableListOf() }.add(str)
        }

        return word_list.values.toList()
    }
}
