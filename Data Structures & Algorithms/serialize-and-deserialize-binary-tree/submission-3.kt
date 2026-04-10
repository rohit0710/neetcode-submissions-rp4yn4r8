/**
 * Definition for a binary tree node.
 * class TreeNode(var `val`: Int) {
 *     var left: TreeNode? = null
 *     var right: TreeNode? = null
 * }
 */

class Codec() {
    // Encodes a URL to a shortened URL.
    fun serialize(root: TreeNode?): String {
        val data = mutableListOf<String>()

        fun helper(root: TreeNode?) {
            if(root == null) {
                data.add("None")
                return
            }

            data.add(root.`val`.toString())
            helper(root.left)
            helper(root.right)
        }
        helper(root)
        print(data.toString())
        println(data.joinToString(", "))
        return data.joinToString(", ")
    }

    // Decodes your encoded data to tree.
    fun deserialize(data: String): TreeNode? {
        val data = data.split(", ").toMutableList()

        fun helper(root: TreeNode?): TreeNode?
        {
            if(data[0] == "None"){
                data.removeFirst()
                return null
            }

            val root = TreeNode(data.removeFirst().toInt())
            root.left = helper(root)
            root.right = helper(root)

            return root
        }
        return helper(null)
    }
}
