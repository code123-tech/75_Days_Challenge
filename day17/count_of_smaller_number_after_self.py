import bisect


class Solution:
    #     def merge(self,left,right,mid,nums):
    #         i = left
    #         for j in range(mid+1,right+1):
    #             while i<mid+1 and nums[i][0]<nums[j][0]:
    #                 i += 1
    #             self.res[nums[j][1]] += i-left
    #         nums[left:right+1] = sorted(nums[left:right+1])

    #     def mergeSort(self,left,right,nums):
    #         if left<right:
    #             mid = (left+right)//2
    #             self.mergeSort(left,mid,nums)
    #             self.mergeSort(mid+1,right,nums)

    #             self.merge(left,right,mid,nums)

    def countSmaller(self, nums):
        # self.res = [0]*len(nums)
        # nums = nums[::-1]
        # nums = [(val,i) for i,val in enumerate(nums)]
        # self.mergeSort(0,len(nums)-1,nums)
        # return self.res[::-1]
        sor = sorted(nums)
        res = []
        for el in nums:
            index = bisect.bisect_left(sor, el)
            res.append(index)
            sor.pop(index)
        return res


sol = Solution()
print(sol.countSmaller([5, 2, 6, 1]))
