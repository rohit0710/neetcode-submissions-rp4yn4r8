class Solution {
    fun threeSum(nums: IntArray): List<List<Int>> {
        val res = mutableListOf<MutableList<Int>>()
        nums.sort()
        for (i in 0 .. nums.size-3)
            if (i == 0 || nums[i] != nums[i-1]){
                var l = i + 1
                var r = nums.size -1
                while (l < r)
                {
                    if (nums[i] + nums[l] + nums[r] == 0) {
                        res.add(arrayListOf(nums[i], nums[l], nums[r]))
                        while (l < r && nums[l] == nums[l+1])
                            l ++
                        while (l < r && nums[r] == nums[r-1])
                            r--
                        l++
                        r--
                    }
                    else if(nums[i] + nums[l] + nums[r] < 0)
                        l ++
                    else
                        r--
                }
            }

        return res
    }
}
