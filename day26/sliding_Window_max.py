import collections


class Solution:
    def maxSlidingWindow(self, nums, k: int):
        if(k == 1 or len(nums) == 1):
            return nums
        queue = collections.deque()
        maxi = -2147483648
        index = 0
        for i in range(k):
            while queue and nums[i] >= nums[queue[-1]]:
                queue.pop()
            queue.append(i)
        answer = []
        for i in range(k, len(nums)):
            answer.append(nums[queue[0]])
            while queue and queue[0] <= i-k:
                queue.popleft()
            while queue and nums[i] >= nums[queue[-1]]:
                queue.pop()
            queue.append(i)
        answer.append(nums[queue[0]])
        return answer


sol = Solution()
print(sol.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
