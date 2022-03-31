class Solution:
    def findDuplicates(self, nums):
        result = []
        size = len(nums)

        for i in range(size):
            number = abs(nums[i])-1
            if nums[number] < 0:
                result.append(number+1)

            nums[number] = -nums[number]
        return result


sol = Solution()
nums = [4, 3, 2, 7, 8, 2, 3, 1]
print(sol.findDuplicates(nums))
