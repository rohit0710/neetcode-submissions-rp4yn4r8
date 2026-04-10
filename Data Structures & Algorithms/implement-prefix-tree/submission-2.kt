class TrieNode(var ch: String = "", var isEnd: Boolean = false){
    val children: MutableMap<String, TrieNode> = mutableMapOf()
}
class PrefixTree {
    val root = TrieNode()

    fun insert(word: String) {
        var node: TrieNode = root
        for (w in word){
            node = node.children.getOrPut(w.toString()) { TrieNode(w.toString())}
        }
        node.isEnd = true
    }

    fun search(word: String): Boolean {
        var node: TrieNode = root
        for (w in word) {
            node = node.children[w.toString()] ?: return false
        }
        return node.isEnd
    }

    fun startsWith(prefix: String): Boolean {
        var node: TrieNode = root
        for (w in prefix) {
            node = node.children[w.toString()] ?: return false
        }
        return true
    }
}
