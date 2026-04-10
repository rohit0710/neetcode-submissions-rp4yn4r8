class TrieNode(var ch: String = "", var isEnd: Boolean = false){
    val children: MutableMap<String, TrieNode> = mutableMapOf()
}
class WordDictionary {
val root = TrieNode()

    fun addWord(word: String) {
        var node: TrieNode = root
        for (w in word){
                node = node.children.getOrPut(w.toString()) { TrieNode(w.toString())}
        }
        node.isEnd = true
    }

    fun search(word: String): Boolean {
        fun dfs(node: TrieNode, word: String): Boolean
        {
            var node = node
            for ((i,w) in word.withIndex()) {
                if (w.toString() == ".") {
                    for (wildcard in node.children.keys)
                        if (dfs(node.children.getValue(wildcard), word.substring(i+1)))
                            return true
                    return false
                }
                else
                    node = node.children[w.toString()] ?: return false
            }
            return node.isEnd
        }
        return dfs(root, word)
    }


}
