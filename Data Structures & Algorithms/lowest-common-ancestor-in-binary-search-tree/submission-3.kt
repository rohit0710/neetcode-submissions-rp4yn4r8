/**
 * Definition for a binary tree node.
 * class TreeNode(var `val`: Int) {
 *     var left: TreeNode? = null
 *     var right: TreeNode? = null
 * }
 */

class Solution {
    fun lowestCommonAncestor(root: TreeNode?, p: TreeNode?, q: TreeNode?): TreeNode? {
        var root = root
        while(root != null){
            if(p!!.`val` < root.`val` && q!!.`val` < root.`val`)
                root = root.left
            else if(p!!.`val` > root.`val` && q!!.`val` > root.`val`)
                root = root.right
            else
                return root
        }
        return null
    }
}
