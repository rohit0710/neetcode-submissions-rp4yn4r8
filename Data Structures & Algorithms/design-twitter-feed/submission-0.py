class Twitter:

    def __init__(self):
        self.tweet_data = defaultdict(list)
        self.follow_data = defaultdict(set)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweet_data[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        res = []
        friends = self.follow_data[userId] | {userId}
        for friend_id in friends:
            for time, tweet_id in self.tweet_data[friend_id]:
                heapq.heappush(heap, (time, tweet_id))
                if len(heap) > 10:
                    heapq.heappop(heap)
            
        while heap:
            res.append(heapq.heappop(heap)[1])
        
        return res[::-1]


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.follow_data[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follow_data[followerId]:
            self.follow_data[followerId].remove(followeeId)
