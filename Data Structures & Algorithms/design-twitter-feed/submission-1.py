import heapq
class Twitter:

    def __init__(self):
        self.count = 0
        self.followMap = defaultdict(set) # user: set of followeeId
        self.tweetMap = defaultdict(list) # user: list of [count, tweetId]


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1
        

    def getNewsFeed(self, userId: int) -> List[int]:

        res = [] # ordered starting from most recent
        minHeap = [] # used to identify most recent

        # get lists of tweets from user and their following
        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            idx = len(self.tweetMap[followeeId]) - 1

            if idx >= 0:
                count, tweetId = self.tweetMap[followeeId][idx]
                minHeap.append([count, tweetId, followeeId, idx - 1]) # pos of next most recent tweet
        heapq.heapify(minHeap)
        while minHeap and len(res) < 10:
            count, tweetId, followeeId, idx = heapq.heappop(minHeap)
            res.append(tweetId)
            count, tweetId = self.tweetMap[followeeId][idx]

            if idx >= 0:
                heapq.heappush(minHeap, [count, tweetId, followeeId, idx - 1])
            
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
        
