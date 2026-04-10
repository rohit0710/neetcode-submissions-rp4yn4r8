# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preOrder: List[int], inOrder: List[int]) -> Optional[TreeNode]:
        inOrder_map = dict()
        for i, v in enumerate(inOrder):
            inOrder_map[v] = i
        self.ind = 0

        def helper(left, right):
            if left > right:
                return

            root = TreeNode(preOrder[self.ind])
            self.ind += 1

            root.left = helper(left, inOrder_map[root.val] - 1)
            root.right = helper(inOrder_map[root.val] + 1, right)
            
            return root
        
        return helper(0, len(preOrder)-1)