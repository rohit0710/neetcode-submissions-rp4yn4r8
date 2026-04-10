# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = float('-inf')
        def helper(root):
            if not root:
                return 0

            l  = helper(root.left)
            r = helper(root.right)

            lr_max = max(l , r)
            rootmax = max(root.val, lr_max + root.val)
            all_max = max(rootmax, root.val + l + r)

            self.res = max(self.res, all_max)

            return rootmax
        helper(root)
        return self.res