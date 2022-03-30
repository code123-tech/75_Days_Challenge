# Approach 1 - Dynamic Programming with memoization
'''
Just remove either add first element, or add last element, adn find max among them.
Time - O(2**k)
TLE 
'''
'''
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        dp = {}
    
        def answer(cd,left,right,k,sum_):
            if right<0 or left>=len(cd) or k==0:
                return sum_
            
            if (left,right,k,sum_) in dp:
                return dp[(left,right,k,sum_)]
            
            maxi = max(answer(cd,left+1,right,k-1,sum_ + cd[left]),answer(cd,left,right-1,k-1,sum_ + cd[right]))
            dp[(left,right,k,sum_)] = maxi
            return maxi
        return answer(cardPoints,0,len(cardPoints)-1,k,0)
'''
# Approach 2 - Sliding Window Concept
'''
In this, we have find a subarray whose sum is minimum and that should be of length n-k.
and thus we will remain with maximum sum.
Time - O(n) [n = length  of given list]
Space - O(1)
'''


class Solution:
    def maxScore(self, cardPoints, k):
        n = len(cardPoints)
        length = n-k
        tempSum = sum(cardPoints[:length])

        mini = tempSum

        for i in range(length, len(cardPoints)):
            tempSum -= cardPoints[i-length]
            tempSum += cardPoints[i]
            mini = min(tempSum, mini)

        return sum(cardPoints)-mini


sol = Solution()
nums = [2, 3, 1, 1, 4]
print(sol.maxScore(nums, 2))
