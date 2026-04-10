# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def helper(root):
            if not root:
                return TreeNode(val)
            if val > root.val:
                root.right = helper(root.right)
            else:
                root.left = helper(root.left)
                    
            return root
        return helper(root)