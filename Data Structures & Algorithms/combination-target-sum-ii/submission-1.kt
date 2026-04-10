class Solution {
    fun combinationSum2(nums: IntArray, target: Int): List<List<Int>> {
        val res = mutableListOf<List<Int>>()
        fun helper(temp: List<Int>, ind: Int){
            if(temp.sum() == target)
                res.add(temp)
            if(temp.sum() > target)
                return 
            for(i in ind until nums.size)
                if (i == ind || nums[i-1]!=nums[i])
                helper(temp + nums[i], i+1)
        }
        nums.sort()
        helper(arrayListOf(), 0)
        return res
    }
}
