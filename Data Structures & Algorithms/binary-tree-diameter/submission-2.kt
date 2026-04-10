/**
 * Definition for a binary tree node.
 * class TreeNode(var `val`: Int) {
 *     var left: TreeNode? = null
 *     var right: TreeNode? = null
 * }
 */

class Solution {
    fun diameterOfBinaryTree(root: TreeNode?): Int {
        var ans = Int.MIN_VALUE
        fun maxDepth(root: TreeNode?): Int {        
        if(root == null) {
            return 0
        }
        val l = maxDepth(root.left)
        val r = maxDepth(root.right)

        ans = maxOf(ans, l + r)
        return 1+ maxOf(l, r)
    }
    maxDepth(root)
    return ans
    }
}
