class Solution:
    def jump(self, nums):
        if len(nums) <= 1:
            return 0

        jumps = 1
        start = 0
        end = 1

        for i in range(start, end):
            if i+nums[i] >= len(nums)-1:
                return jumps
            start, end = end, i+nums[i]

        while end < len(nums)-1:
            jumps += 1
            maxend = end+1
            for i in range(start, end+1):
                if i + nums[i] >= len(nums)-1:
                    return jumps
                maxend = max(maxend, i+nums[i])
            start, end = end+1, maxend

        return jumps


sol = Solution()
nums = [2, 3, 1, 1, 4]
print(sol.jump(nums))
