# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def checkBalance(root):
            if not root:
                return (True,0)
            islBalanced, l = checkBalance(root.left) 
            isrBalanced, r = checkBalance(root.right)

            isBalanced = islBalanced and isrBalanced and abs(l - r) <= 1

            return (isBalanced, 1+ max(l, r))
        return checkBalance(root)[0]
