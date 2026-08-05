# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        data = []

        def helper(root):
            if not root:
                data.append("None")
                return
            
            data.append(str(root.val))
            helper(root.left)
            helper(root.right)
        
        helper(root)
        return ", ".join(data)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data = data.split(", ")

        def build(root):
            if data[0] == "None":
                data.pop(0)
                return None
            
            root = TreeNode(int(data.pop(0)))
            root.left = build(root)
            root.right = build(root)

            return root

        return build(None)