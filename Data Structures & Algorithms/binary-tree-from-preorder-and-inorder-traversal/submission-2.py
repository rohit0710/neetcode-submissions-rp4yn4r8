# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preOrder: List[int], inOrder: List[int]) -> Optional[TreeNode]:
        inorder_map = defaultdict()
        for i,v in enumerate(inOrder):
            inorder_map[v] = i

        ind=0
        def build(low, high):
            nonlocal ind
            if low > high:
                return

            val = preOrder[ind]
            ind += 1
            
            root = TreeNode(val)
            root.left = build(low, inorder_map[val]-1)
            root.right = build(inorder_map[val]+1, high)
            
            return root
        
        return build(0, len(preOrder)-1)
                        
