from collections import defaultdict


class Solution:
    def subarraysWithKDistinct(self, nums, k: int) -> int:
        # [1,2,3,1,2]

        # [1,2,1,3,4]  k = 3

        # subarrayWithAtmostKDifferentElements - subarrayWithAtmostK-1DifferentElements

        def count_sub_with_at_K_diff_int(K):
            dicti = defaultdict(int)
            left = 0
            result = 0
            for right in range(len(nums)):
                if dicti[nums[right]] == 0:
                    K -= 1

                dicti[nums[right]] += 1

                while K < 0:
                    dicti[nums[left]] -= 1
                    if dicti[nums[left]] == 0:
                        K += 1

                    left += 1
                result += right - left + 1
            return result

        return count_sub_with_at_K_diff_int(k) - count_sub_with_at_K_diff_int(k-1)


sol = Solution()
print(sol.subarraysWithKDistinct([1, 2, 1, 3, 4], 3))
