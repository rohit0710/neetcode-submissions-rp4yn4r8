class TrieNode:
    def __init__(self,ch = "", end = False):
        self.ch = ch
        self.end = end
        self.children = defaultdict(TrieNode)

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        node = self.root
        for w in word:
            if w not in node.children:
                node.children[w] = TrieNode(ch = w)
            node = node.children[w]
        node.end = True

class Solution():
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.addWord(word)
        m,n = len(board), len(board[0])
        def dfs(i,j, node, word):
            if not 0 <= i < m or not 0 <= j < n or (i,j) in visited or board[i][j] not in node.children:
                return 
            
            node = node.children[board[i][j]]
            word += board[i][j]
            visited.add((i,j))
            if node.end:
                res.add(word)

            dfs(i-1,j, node, word)
            dfs(i+1,j, node, word)
            dfs(i,j-1, node, word)
            dfs(i,j+1, node, word)

            visited.remove((i,j))

            return
            
        visited = set()
        res = set()
        for i in range(m):
            for j in range(n):
                dfs(i,j, trie.root, "")
        
        return list(res)