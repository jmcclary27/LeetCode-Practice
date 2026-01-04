class Twitter:

    def __init__(self):
        self.counter = 0
        self.tweets = defaultdict(list)
        self.follows = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.counter += 1
        self.tweets[userId].append((self.counter * -1, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        self.counter += 1
        feed = list(self.tweets[userId])
        for user in self.follows[userId]:
            feed.extend(self.tweets[user])
        heapq.heapify(feed)

        recentTweets = []
        i = 0
        while i < 10 and feed:
            recentTweets.append(heapq.heappop(feed)[1])
            i += 1
        return recentTweets

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId and followeeId not in self.follows[followerId]:
            self.follows[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId and followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)