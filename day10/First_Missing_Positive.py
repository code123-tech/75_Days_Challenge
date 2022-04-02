class Solution:
    def firstMissingPositive(self, nums) -> int:
        mini = float('inf')
        maxi = float('-inf')
        size = len(nums)
        dicti = {}
        for i in range(size):
            if nums[i] > 0:
                mini = min(mini, nums[i])
                maxi = max(maxi, nums[i])
                dicti[nums[i]] = 1

        if (mini == float('inf') and 1 not in dicti) or mini >= 2:
            return 1

        for num in range(mini, maxi+1):
            if num not in dicti:
                return num
            else:
                num += 1
        return num


sol = Solution()
nums = [1, 2, 0]
print(sol.firstMissingPositive(nums))
