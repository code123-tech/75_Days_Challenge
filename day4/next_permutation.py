class Solution:

    def findNextGreatElement(self, nums, number, index):
        tempIn = 0
        for i in range(len(nums)-1, index, -1):
            if nums[i] > number:
                tempIn = i
                break
        return tempIn

    def nextPermutation(self, nums):
        # Step:1 Find the First smallest number from next to it from backwards.
        i = len(nums)-2
        while i >= 0:
            if nums[i] < nums[i+1]:
                break
            i -= 1
        else:
            # If not found then sort array and return
            nums.sort()
            return
        # Step 2: Now find the next Index grater then tarIndex, and element should be greater
        tarIndex = i
        next_index = self.findNextGreatElement(nums, nums[tarIndex], tarIndex)
        # step 3: Swap target and nextIndex value
        nums[tarIndex], nums[next_index] = nums[next_index], nums[tarIndex]
        i = tarIndex+1
        j = len(nums)-1
        # Step 4: Now reverse from tarIndex+1 to lastIndex
        nums[tarIndex+1:] = nums[tarIndex+1:][::-1]


sol = Solution()
nums = [1, 2, 3]
sol.nextPermutation(nums)
