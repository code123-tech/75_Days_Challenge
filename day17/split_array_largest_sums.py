class Solution:
    def splitArray(self, nums, m: int) -> int:
        # Case 1
        # So, As we can see by the constraint of m itself, that maximum parts of the given array can be total length of the
        # array, In that case, the maximum number present in the array will be the required answer.

        # Case 2
        # So, As we can see by the constraint of m itself, that minimum parts of the given array can be 1 of the
        # array, In that case, the sum of all number present in the array will be the required answer.

        # So, our answer lies between max(nums)  to sum(nums)

        # By contraints, range could be [0, 10^9]

        # So, It can be reduced to [max(nums),sum(nums)]
        left = max(nums)
        right = sum(nums)

        # Now, you have to check for mid value, that if that number is the actual number which will give number of splits less than given number

        def isValidAnswer(mid):
            sum_ = 0
            splits = 1
            for el in nums:
                if sum_ + el <= mid:
                    sum_ = sum_ + el
                else:
                    sum_ = el
                    splits += 1
            return splits <= m

        required_answer = left
        while left <= right:
            mid = (left+right)//2

            if isValidAnswer(mid):
                required_answer = mid
                right = mid-1
            else:
                left = mid+1
        return required_answer


sol = Solution()
print(sol.splitArray([5, 2, 6, 1], 2))
