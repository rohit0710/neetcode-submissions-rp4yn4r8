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
        def inOrder(root):
            if not root:
                return
            
            inOrder(root.left)
            self.res.append(root.val)
            inOrder(root.right)

            return root
        
        inOrder(root)
        return self.res[k-1]