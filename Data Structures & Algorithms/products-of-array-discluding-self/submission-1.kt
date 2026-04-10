class Solution {
    fun productExceptSelf(nums: IntArray): IntArray {
val res = IntArray(nums.size){ 1 }
        var left = 1
        var right = 1
        
        for ((i, n) in nums.withIndex())
        {
            res[i] *= left
            left *= n
        }

        for (i in nums.size-1 downTo 0)
        {
            res[i] *= right
            right *= nums[i]
        }
        
        return res
    }
}
