# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.res = []
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def helper(root):
            if not root:
                return

            if root.left: helper(root.left)
            self.res.append(root.val)
            if root.right: helper(root.right)

            return root
        
        helper(root)
        return self.res[k-1]