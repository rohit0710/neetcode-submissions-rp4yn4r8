# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        serialized = []
        def serialize(root):
            nonlocal serialized
            if not root:
                serialized.append("None")
                return

            serialized.append(str(root.val))
            serialize(root.left)
            serialize(root.right)

            return root

        serialize(root)
        str_root = ", ".join(serialized)
        serialized = []
        serialize(subRoot)
        str_sr = ", ".join(serialized)
        print(str_root)
        print(str_sr)
        return str_sr in str_root