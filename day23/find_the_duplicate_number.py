class Solution:
    def findDuplicate(self, nums) -> int:

        #         nums = [1,3,4,2,2]

        #         nums i = 0 = [1, -3, 4, 2, 2]
        #         i = 1   [1,3,4,-2,2]

        #         i = 2, [1,3,4,-2,-2]

        #         i = 3, [1,3,-4,2,]

        # [2,1,1]
        # i = 0,  [2,1,-1]
        # i = 1, [2,-1,-1]
        # i = 2, [2,-1,-1]
        size = len(nums)
        for i in range(size):
            number = abs(nums[i])
            # print(number,nums[number],nums)
            if nums[number] < 0:
                return number
            else:
                nums[number] = -nums[number]
