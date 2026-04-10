/**
 * Definition for a binary tree node.
 * class TreeNode(var `val`: Int) {
 *     var left: TreeNode? = null
 *     var right: TreeNode? = null
 * }
 */

class Solution {
    fun rightSideView(root: TreeNode?): List<Int> {
        val res = mutableListOf<Int>()
        if(root == null)
            return res
        var root = root
        val que = ArrayDeque<TreeNode>()
        que.add(root)
        var temp = 0
        while(!que.isEmpty()){
            for (i in 0 .. que.size -1)
            {
                val root = que.removeFirst()
                temp = root.`val`
                if(root.left != null) que.add(root.left)
                if(root.right != null) que.add(root.right)
            }
            res.add(temp)
        }
        return res
    }
}
