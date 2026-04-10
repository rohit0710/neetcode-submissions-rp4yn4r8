/**
 * Definition for a binary tree node.
 * class TreeNode(var `val`: Int) {
 *     var left: TreeNode? = null
 *     var right: TreeNode? = null
 * }
 */

class Solution {
    fun kthSmallest(root: TreeNode?, k: Int): Int {
        val res = mutableListOf<Int>()
        fun dfs(root: TreeNode?): TreeNode? {
            if (root== null)
                return null    
            
            dfs(root.left)
            res.add(root.`val`)
            dfs(root.right)

            return root
        }
        dfs(root)
        return res[k-1]
    }
}
