class Solution:
    def search(self, nums, target: int) -> int:
        if(nums == None or len(nums) == 0):
            return -1

        low = 0
        high = len(nums)-1

        while(low <= high):
            mid = low + (high-low)//2
            if(nums[mid] == target):
                return mid
            if(nums[mid] >= nums[low]):
                if(target >= nums[low] and target < nums[mid]):
                    high = mid-1
                else:
                    low = mid+1
            else:
                if(target <= nums[high] and target > nums[mid]):
                    low = mid+1
                else:
                    high = mid-1
        return -1


sol = Solution()
nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
print(sol.search(nums, target))
