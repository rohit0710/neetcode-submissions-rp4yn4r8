class TrieNode:
    def __init__(self, ch = "", is_end = False):
        self.ch = ch
        self.children = {}
        self.is_end = is_end

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        node = self.root
        for w in word:
            if w not in node.children:
                node.children[w] = TrieNode(ch = w)
            node = node.children[w]
        node.is_end = True

class Solution:
    def findWords(self, board: List[List[str]], wordList: List[str]) -> List[str]:
        visited= set()
        res = set()
        trie = Trie()
        for word in wordList:
            trie.addWord(word)
        m,n = len(board), len(board[0])

        def dfs(i,j, word, node):
            if (not 0 <= i < m) or (not 0 <= j <n) or (i,j) in visited or board[i][j] not in node.children:
                return

            visited.add((i,j))
            node = node.children[board[i][j]]
            word += board[i][j]
            if node.is_end:
                res.add(word)

            dfs(i+1,j,word, node)
            dfs(i-1,j,word, node)
            dfs(i,j+1,word, node)
            dfs(i,j-1,word, node)

            visited.remove((i,j))

            return

        for i in range(m):
            for j in range(n):
                dfs(i,j,"", trie.root)

        return list(res)
