class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for w in word:
            if w in node.children:
               node = node.children[w]
            else:
                new_node = TrieNode(w)
                node.children[w] = new_node
                node = new_node

        node.end = True

    def search(self, word: str) -> bool:
        node = self.root
        for w in word:
            if w in node.children:
               node = node.children[w]
            else:
                return False
        return True if node.end == True else False

    def startsWith(self, prefix: str) -> bool:

        node = self.root
        for w in prefix:
            if w in node.children:
               node = node.children[w]
            else:
                return False
        return True 


class TrieNode:
    def __init__(self,ch = "", end = False):
        self.ch = ch
        self.end = end
        self.children = defaultdict(TrieNode)
