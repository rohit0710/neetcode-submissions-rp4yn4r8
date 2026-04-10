# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        self.res = []
        def helper(root):
            if not root:
                self.res.append("None")
                return

            self.res.append(str(root.val))
            helper(root.left)
            helper(root.right)

            return root

        helper(root)
        return ", ".join(self.res)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> TreeNode:
        data = deque(data.split(", "))
        if not data or data == "":
            return
        def helper(root):
            val = data.popleft()

            if val != "None":
                node = TreeNode(val)
                node.left = helper(node)
                node.right = helper(node)
            else:
                return None

            return node

        return helper(None)
