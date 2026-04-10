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
    
        def getMax(root):
            if not root:
                return 0
            
            left = getMax(root.left)
            right = getMax(root.right)

            self.ans= max(self.ans, left+ right)

            return 1 + max(left, right)
        getMax(root)
        return self.ans