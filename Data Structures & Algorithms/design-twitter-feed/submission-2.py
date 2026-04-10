class Twitter:

    def __init__(self):
        self.user_data = defaultdict(list)
        self.follower_map = defaultdict(set)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.user_data[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        feed_people = self.follower_map[userId] | {userId}
        heap = []
        for user in feed_people:
            for tweet in self.user_data[user]:
                heapq.heappush(heap, tweet)
                if len(heap) > 10:
                    heapq.heappop(heap)
        res = []

        while heap:
            res.append(heapq.heappop(heap)[-1])
        
        return res[::-1]
         
    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId != followerId:
            self.follower_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follower_map[followerId]:
            self.follower_map[followerId].remove(followeeId)
