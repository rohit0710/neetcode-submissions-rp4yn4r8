# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.ans = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def getDiameter(root):
            if not root:
                return 0
            l = getDiameter(root.left) 
            r = getDiameter(root.right)
            self.ans = max(self.ans, l + r)

            return 1 + max(l, r)
        getDiameter(root)
        return self.ans