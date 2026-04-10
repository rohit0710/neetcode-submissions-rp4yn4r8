# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preOrder: List[int], inOrder: List[int]) -> Optional[TreeNode]:
        in_map = dict()
        for i,v in enumerate(inOrder):
            in_map[v] = i

        preord_ind = 0
        def helper(low, high):
            nonlocal preord_ind
            if low > high:
                return

            val = preOrder[preord_ind]
            preord_ind += 1
            root = TreeNode(val)
            root.left = helper(low, in_map[val]-1)
            root.right = helper(in_map[val]+1, high)

            return root
        return helper(0, len(preOrder)-1)