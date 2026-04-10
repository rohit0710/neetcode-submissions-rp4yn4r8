# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res= []
        if not root:
            return []
        que = deque()
        que.append(root)

        while que:
            temp = []
            for i in range(len(que)):
                root = que.popleft()
                temp.append(root.val)
                if root.left: que.append(root.left)
                if root.right: que.append(root.right)
            res.append(temp)
        return res