class Solution:
    def peakIndexInMountainArray(self, arr) -> int:
        size = len(arr)
        left = 0
        right = size - 1
        while left < right:
            mid = (left+right)//2
            if arr[mid] < arr[mid+1]:
                left = mid+1
            else:
                right = mid
        return left


sol = Solution()
arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(sol.peakIndexInMountainArray(arr))
