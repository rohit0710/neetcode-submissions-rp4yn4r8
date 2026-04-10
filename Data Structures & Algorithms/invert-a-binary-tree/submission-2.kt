/**
 * Definition for a binary tree node.
 * class TreeNode(var `val`: Int) {
 *     var left: TreeNode? = null
 *     var right: TreeNode? = null
 * }
 */

class Solution {
    fun invertTree(root: TreeNode?): TreeNode? {
        fun helper(root: TreeNode?): TreeNode?{
            if(root == null)
                return root
            
            val temp = root.left  
            root.left = root.right
            root.right = temp

            helper(root.left)
            helper(root.right)

            return root
        }

        return helper(root)
    }
}
