class Solution {
    fun subsets(nums: IntArray): List<List<Int>> {
        val res = mutableListOf<List<Int>>()
        fun helper(temp: List<Int>, ind: Int){
            res.add(temp)

            for(i in ind until nums.size)
                helper(temp + nums[i], i + 1)
        }
        helper(arrayListOf(), 0)
        return res
    }
}
