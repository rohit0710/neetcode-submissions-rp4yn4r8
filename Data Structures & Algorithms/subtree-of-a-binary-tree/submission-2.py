# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        res = []
        def serialize(root):
            if not root:
                res.append("None")
                return 
            
            res.append(str(root.val))
            serialize(root.left)
            serialize(root.right)

        serialize(root)
        root_st = ", ".join(res)
        res = []
        serialize(subRoot)
        subroot_st = ", ".join(res)

        return subroot_st in root_st