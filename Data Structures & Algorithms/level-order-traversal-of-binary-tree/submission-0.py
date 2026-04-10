# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        queue.append(root)
        res = []
        if not root:
            return res
        
        while queue:
            temp = []
            for i in range(len(queue)):
                root = queue.popleft()
                temp.append(root.val)
                if root.left: queue.append(root.left)
                if root.right: queue.append(root.right)
            res.append(temp)
        
        return res
