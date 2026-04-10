/**
 * Definition for a binary tree node.
 * class TreeNode(var `val`: Int) {
 *     var left: TreeNode? = null
 *     var right: TreeNode? = null
 * }
 */

class Solution {
    fun isBalanced(root: TreeNode?): Boolean {
        fun balance(root: TreeNode?): Pair<Boolean, Int>{
            if(root==null)
                return Pair(true, 0)
            
            val (isLBalanced, lHeight) = balance(root.left)
            val (isRBalanced, rHeight) = balance(root.right)

            val isBalanced = isLBalanced && isRBalanced && abs(lHeight - rHeight) <= 1

            return Pair(isBalanced, 1 + maxOf(lHeight,rHeight))
        }
        return balance(root).first
    }
}
