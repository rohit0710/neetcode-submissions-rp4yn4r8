# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subroot: Optional[TreeNode]) -> bool:
        res = []
        def serialize(root):
            if not root:
                res.append("None")
                return 
            
            res.append(str(root.val))
            serialize(root.left)
            serialize(root.right)
            
            return root
        
        serialize(root)
        root_st = ", ".join(res)
        res = []
        serialize(subroot)
        sub_root_st = ", ".join(res)
        
        return sub_root_st in root_st