# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = float('-inf')
        def dfs(root):
            if not root:
                return 0
            
            l = dfs(root.left)
            r = dfs(root.right)

            lr_max= max(l,r)
            root_max = max(root.val, root.val + lr_max)
            all_max = max(root_max, root.val + l + r)

            self.res = max(self.res, all_max)

            return root_max
        dfs(root)
        return self.res