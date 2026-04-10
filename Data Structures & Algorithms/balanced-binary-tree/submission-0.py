# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(root):
            if not root:
                return (True, 0)
            
            is_left_balanced, l_height = helper(root.left)
            is_right_balanced, r_height = helper(root.right)

            is_balanced = is_left_balanced and is_right_balanced and abs(l_height-r_height) <= 1

            return (is_balanced, 1 + max(l_height, r_height))
        return helper(root)[0]