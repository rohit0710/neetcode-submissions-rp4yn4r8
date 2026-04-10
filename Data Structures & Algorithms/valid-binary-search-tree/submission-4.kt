/**
 * Definition for a binary tree node.
 * class TreeNode(var `val`: Int) {
 *     var left: TreeNode? = null
 *     var right: TreeNode? = null
 * }
 */

class Solution {
    fun isValidBST(root: TreeNode?): Boolean {
        fun isValid(root:TreeNode?, low: Int, high: Int): Boolean
        {
            if(root == null)
                return true
            
            if (root.`val` <= low || root.`val` >= high)
                return false
            
            return isValid(root.left, low, root.`val`) && isValid(root.right, root.`val`, high)

        }
        return isValid(root, Int.MIN_VALUE, Int.MAX_VALUE)
    }
}
