class Solution:
    def majorityElement(self, nums):

        candidate = nums[0]
        count = 0
        for num in nums:
            if num == candidate:
                count += 1
            elif count == 0:
                candidate = num
                count = 0
            else:
                count -= 1
        return candidate


sol = Solution()
nums = [2, 2, 1, 1, 1, 2, 2]
print(sol.majorityElement(nums))
