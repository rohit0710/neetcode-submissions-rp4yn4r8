/**
 * Definition for a binary tree node.
 * class TreeNode(var `val`: Int) {
 *     var left: TreeNode? = null
 *     var right: TreeNode? = null
 * }
 */

class Solution {
    fun goodNodes(root: TreeNode?): Int {
        var count = 0
        fun dfs(root: TreeNode?, maxVal: Int): TreeNode? {
            if (root == null)
                return null
            if (maxVal <= root.`val`)
                count ++

            val newMaxVal = maxOf(maxVal, root.`val`)
            dfs(root.left, newMaxVal)
            dfs(root.right, newMaxVal)
            return root
        }
        if (root != null) {
             dfs(root, root.`val`)
        }
        return count
    }
}
