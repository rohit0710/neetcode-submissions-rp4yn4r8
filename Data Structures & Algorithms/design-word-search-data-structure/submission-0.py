class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
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
        def search_wildcard(node, word):
            for i, w in enumerate(word):
                if w in node.children:
                    node = node.children[w]
                elif w == ".":
                    for nei in node.children:
                        if search_wildcard(node.children[nei], word[i+1: ]):
                            return True
                    return False
                else:
                    return False
            return True if node.end == True else False
        return search_wildcard(node, word)

class TrieNode:
    def __init__(self,ch = "", end = False):
        self.ch = ch
        self.end = end
        self.children = defaultdict(TrieNode)
