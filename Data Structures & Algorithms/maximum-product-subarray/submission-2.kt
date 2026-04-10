class Solution {
    fun maxProduct(nums: IntArray): Int {
        var min_so_far = nums[0]
        var max_so_far = nums[0]
        var res = max_so_far

        for (i in 1 until nums.size){
            var n = nums[i]
            var temp = maxOf(n, n * min_so_far, n*max_so_far)
            min_so_far = minOf(n, n * max_so_far, n *  min_so_far)
            max_so_far = temp
            res = maxOf(res, max_so_far)
        }
        return res
    }   
}
