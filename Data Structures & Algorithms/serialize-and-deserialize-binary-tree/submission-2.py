# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        def helper(root):
            if not root:
                res.append("None")
                return 
            
            res.append(str(root.val))
            helper(root.left)
            helper(root.right)
            
        helper(root)
        return ", ".join(res)


    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> TreeNode:
        data = data.split(", ")
        self.pos = 0

        def helper(root):
            if data[0] == "None":
                data.pop(0)
                return None

            root = TreeNode(int(data.pop(0)))
            root.left = helper(root)
            root.right = helper(root)

            return root
        return helper(None)