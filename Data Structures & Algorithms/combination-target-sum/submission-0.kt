class Solution {
    fun combinationSum(nums: IntArray, target: Int): List<List<Int>> {
        val res = mutableListOf<List<Int>>()
        fun helper(temp: List<Int>, ind: Int){
            if(temp.sum() == target)
                res.add(temp)
            if(temp.sum() > target)
                return 
            for(i in ind until nums.size)
                helper(temp + nums[i], i)
        }
        helper(arrayListOf(), 0)
        return res
    }
}
