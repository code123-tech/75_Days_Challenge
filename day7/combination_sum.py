class Solution:
    def combinationSum(self, candidates, target):

        size = len(candidates)
        result = []

        def backtrack(curIndex, target, curList):
            if target == 0:
                result.append(curList)
                return
            if curIndex == size or target < candidates[curIndex]:
                return
            backtrack(curIndex, target -
                      candidates[curIndex], curList + [candidates[curIndex]])
            backtrack(curIndex+1, target, curList)

        candidates.sort()

        backtrack(0, target, [])
        return result


sol = Solution()
print(sol.combinationSum([2, 3, 6, 7], 7))
