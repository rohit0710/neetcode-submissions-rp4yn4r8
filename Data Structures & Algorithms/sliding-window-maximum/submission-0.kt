class Solution {
    fun maxSlidingWindow(nums: IntArray, k: Int): IntArray {
if (k == 1)
            return nums
        val res = mutableListOf<Int>()
        val que = ArrayDeque<Int>()

        for (i in 0..k-1) {
            while (que.isNotEmpty() && nums[que.last()] <= nums[i])
                que.removeLast()
            que.add(i)
        }
        res.add(nums[que.first()])

        for (i in k until nums.size)
        {
            while (que.isNotEmpty() && que.first() <= i - k)
                que.removeFirst()

            while (que.isNotEmpty() && nums[que.last()] <= nums[i])
                que.removeLast()
            que.add(i)
            
            res.add(nums[que.first()])
        }
    return res.toIntArray()
    }
}
