/**
 * Definition for a binary tree node.
 * class TreeNode(var `val`: Int) {
 *     var left: TreeNode? = null
 *     var right: TreeNode? = null
 * }
 */

class Solution {
    fun maxPathSum(root: TreeNode?): Int {
        var res = Int.MIN_VALUE
        fun helper(root: TreeNode?): Int {
            if(root==null)
                return 0
            
            val l = helper(root.left)
            val r = helper(root.right)

            val lr_max = maxOf(l, r)
            val root_max= maxOf(root.`val`, root.`val` + lr_max)
            val all_max = maxOf(root_max, root.`val` +  + l+ r)

            res = maxOf(res, all_max)

            return root_max
        }
        helper(root)
        return res

    }
}
