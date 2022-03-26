class Solution:
    def threeSum(self, nums):
        nums.sort()
        size = len(nums)
        result = []
        for i in range(size-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            else:
                left = i+1
                right = size-1
                while left < right:
                    sum = nums[i] + nums[left]+nums[right]
                    if sum < 0:
                        left += 1
                    elif sum > 0:
                        right -= 1
                    else:
                        result.append([nums[i], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left+1]:
                            left += 1
                        while left < right and nums[right] == nums[right-1]:
                            right -= 1
                        left += 1
                        right -= 1
        return result


sol = Solution()
print(sol.threeSum([-1, 0, 1, 2, -1, -4]))
