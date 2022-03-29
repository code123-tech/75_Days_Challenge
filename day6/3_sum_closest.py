class Solution:
    def threeSumClosest(self, nums, target):
        # [-1,2,1,4]  target = 1

        # one number, find next two number sum which is closes to target-number

        nums.sort()
        size = len(nums)
        result = float('inf')
        for i in range(size):
            curr = nums[i]
            left = i+1
            right = size-1
            while left < right:
                currSum = curr + nums[left] + nums[right]
                if abs(target-currSum) < abs(result):
                    result = target-currSum
                if currSum > target:
                    right -= 1
                else:
                    left += 1
            if result == 0:
                return target-result
        return target-result


sol = Solution()
nums = [-1, 2, 1, 4]
target = 1
print(sol.threeSumClosest(nums, target))
