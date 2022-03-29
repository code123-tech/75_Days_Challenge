class Solution:
    def fourSum(self, nums, target):
        size = len(nums)
        if size < 4:
            return []

        result = set()
        nums.sort()
        i = 0
        for i in range(size):
            for j in range(i+1, size):
                # Two Sum Logic is written below when given array is sorted.
                tempTarget = target - (nums[i] + nums[j])
                left = j + 1
                right = size - 1
                while left < right:
                    sum_ = nums[left] + nums[right]
                    if sum_ > tempTarget:
                        right -= 1
                    elif sum_ < tempTarget:
                        left += 1
                    else:
                        result.add((nums[i], nums[j], nums[left], nums[right]))

                        while left < size-1 and nums[left] == nums[left+1]:
                            left += 1
                        while right > 0 and nums[right] == nums[right-1]:
                            right -= 1
                        left += 1
                        right -= 1
                while j < size-1 and nums[j] == nums[j+1]:
                    j += 1
            while i < size-1 and nums[i] == nums[i+1]:
                i += 1
        return result


sol = Solution()
nums = [-1, 0, 1, 2, -1, -4]
target = 0
print(sol.fourSum(nums, target))
