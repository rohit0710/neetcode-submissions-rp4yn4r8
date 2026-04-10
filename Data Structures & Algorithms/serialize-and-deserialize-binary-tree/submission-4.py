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
        
        def dfs(root):
            if not root:
                data.append("None")
                return
            
            data.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
            
            return root
        dfs(root)
        return ", ".join(data)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> TreeNode:
        data = data.split(", ")

        def helper(root):
            if data[0] == "None":
                data.pop(0)
                return

            root = TreeNode(int(data.pop(0)))
            root.left = helper(root)
            root.right = helper(root)

            return root

        return helper(None)