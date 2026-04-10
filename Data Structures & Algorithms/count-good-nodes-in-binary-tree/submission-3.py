# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0
        def helper(root, maxv):
            if not root:
                return
            if root.val >= maxv:
                self.res += 1
            
            helper(root.left, max(maxv, root.val))
            helper(root.right, max(maxv, root.val))
            return root
        helper(root, float('-inf'))
        return self.res