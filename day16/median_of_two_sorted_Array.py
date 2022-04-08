class Solution:
    def findMedianSortedArrays(self, array1, array2) -> float:
        if(len(array1) > len(array2)):
            return self.findMedianSortedArrays(array2, array1)
        x = len(array1)
        y = len(array2)
        pm = -2**64
        pp = 2**64
        low = 0
        high = x
        while low <= high:
            partx = (low+high)//2
            party = (x+y+1)//2 - partx

            maxleftx = pm if partx == 0 else array1[partx-1]
            minRightx = pp if partx == x else array1[partx]

            maxlefty = pm if party == 0 else array2[party-1]
            minRighty = pp if party == y else array2[party]

            if(maxleftx <= minRighty and maxlefty <= minRightx):
                if((x+y) & 1 == 0):
                    return (max(maxleftx, maxlefty)+min(minRightx, minRighty))/2
                else:
                    return float(max(maxleftx, maxlefty))
            elif(maxleftx > minRighty):
                high = partx-1
            else:
                low = partx+1


sol = Solution()
print(sol.findMedianSortedArrays(
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
