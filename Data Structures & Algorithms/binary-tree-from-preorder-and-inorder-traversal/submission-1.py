# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preOrder: List[int], inOrder: List[int]) -> Optional[TreeNode]:
        map_in_order = dict()
        for i,v in enumerate(inOrder):
            map_in_order[v] = i
        self.pos = 0
        def helper(left, right):
            if left > right:
                return None
            
            root_val = preOrder[self.pos]
            root = TreeNode(val = root_val)
            pivot = map_in_order[root_val]
            self.pos += 1
            root.left = helper(left, pivot - 1)
            root.right = helper(pivot + 1, right)
            
            return root
        
        return helper(0, len(preOrder)- 1)