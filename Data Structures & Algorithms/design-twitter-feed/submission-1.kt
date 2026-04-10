
class Twitter() {
    val userTweetData = mutableMapOf<Int, MutableList<Pair<Int, Int>>>()
    val followMap = mutableMapOf<Int, MutableSet<Int>>()
    var time = 0

    fun postTweet(userId: Int, tweetId: Int) {
        time++
        userTweetData.getOrPut(userId) {mutableListOf()}.add(Pair(time, tweetId))
    }

    fun getNewsFeed(userId: Int): List<Int> {
        val friends = (followMap[userId] ?: emptySet()) + (userId)
        val pq = PriorityQueue<Pair<Int,Int>>(compareBy { it.first })

        for (f in friends)
            for (info in userTweetData.getOrDefault(f, emptyList<Pair<Int, Int>>())){
                pq.add(info)
                if(pq.size > 10)
                    pq.poll()
            }
        val res = mutableListOf<Int>()
        while(pq.isNotEmpty())
            res.add(pq.poll().second)
        
        return res.reversed()
    }

    fun follow(followerId: Int, followeeId: Int) {
        if(followerId != followeeId)
            followMap.getOrPut(followerId) {mutableSetOf()}.add(followeeId)
    }

    fun unfollow(followerId: Int, followeeId: Int) {
        followMap[followerId]?.remove(followeeId)
    }

}
