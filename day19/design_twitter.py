from collections import defaultdict
import heapq


class Twitter:
    def __init__(self):
        self.timer = 0  # to maintain the time of tweet of a user
        self.tweetMap = defaultdict(list)  # to maintain the tweets of a user
        # to maintain the followers of a user
        self.followMap = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.timer, tweetId])
        self.timer -= 1

    def getNewsFeed(self, userId: int):
        result = []
        miniHeap = []
        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1
                timer, tweetId = self.tweetMap[followeeId][index]
                miniHeap.append([timer, tweetId, followeeId, index-1])

        heapq.heapify(miniHeap)

        while miniHeap and len(result) < 10:
            timer, tweetId, followeeId, index = heapq.heappop(miniHeap)
            result.append(tweetId)
            if index >= 0:
                timer, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(miniHeap, [timer, tweetId, followeeId, index-1])
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
