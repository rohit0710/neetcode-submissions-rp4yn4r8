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
        def dfs(root, temp):
            if not root:
                return
            
            if temp and root.val >= max(temp):
                self.res += 1
            
            dfs(root.left, temp + [root.val])
            dfs(root.right, temp + [root.val])

            return root

        dfs(root, [])
        return self.res