"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        seen = dict()
        def copy(root):
            if not root:
                return None
            if root.val in seen:
                return seen[root.val]
            
            node = Node(root.val)
            seen[root.val] = node
            for nei in root.neighbors:
                node.neighbors.append(copy(nei))

            return node
        
        return copy(node)