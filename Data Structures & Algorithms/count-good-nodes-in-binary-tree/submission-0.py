# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.res = 1
    def goodNodes(self, root: TreeNode) -> int:
        def helper(root, temp_list):
            if not root:
                return 
            
            if temp_list and root.val >= max(temp_list):
                self.res += 1
            
            if root.left: helper(root.left, temp_list+[root.val])
            if root.right: helper(root.right, temp_list+[root.val])
            
            return root
        helper(root, [])
        return self.res