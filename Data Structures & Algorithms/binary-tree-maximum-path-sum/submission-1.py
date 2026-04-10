# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max = float('-inf')
        def dfs(root):
            if not root:
                return 0

            l = dfs(root.left)
            r = dfs(root.right)

            lr_max = max(l, r)
            root_level = max(root.val, root.val + lr_max)
            all_max = max(root_level, l + r + root.val)
            
            self.max = max(self.max, all_max)
            
            return root_level

        dfs(root)
        return self.max