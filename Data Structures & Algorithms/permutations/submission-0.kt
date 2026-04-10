class Solution {
    fun permute(nums: IntArray): List<List<Int>> {
        val res = mutableListOf<List<Int>>()
        fun helper(temp: List<Int>){
            if(temp.size == nums.size)
                res.add(temp)
            
            for(i in 0 until nums.size)
                if(!temp.contains(nums[i]))
                    helper(temp + nums[i])
        }
        helper(arrayListOf())
        return res
    }
}
