from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        #  String s = ABBA, and integer k = 1
        #  index = 0, char = "A"  dict = {A:1}
        #  index = 1, char = "B"  dict = {A:1,B:1}   A = 1, B = 1
        #  index = 2, char = "B"  dict = {A:1,B:2}   A = 1, B = 2
        #  index = 3, char = "A"  dict = {A:2,B:2}   A = 2, B = 2

        # left = 0, right = 0

        # left = 0, right = 1,

        # left = 0, right = 2,

        # left = 0, right = 3,   {A:3,B:1} k = 0

        # left = 1, right = 3,  {A:2,B:1}

        # left = 2, right = 3,  {A:2, B:0}

        counter = defaultdict(int)
        size = len(s)
        left = 0
        maxiFrequency = 0
        result = 0
        for right in range(size):
            counter[s[right]] += 1
            maxiFrequency = max(maxiFrequency, counter[s[right]])
            letterToReplaceInCurrentWindow = (right - left + 1) - maxiFrequency
            if letterToReplaceInCurrentWindow > k:
                counter[s[left]] -= 1
                left += 1
            result = max(result, right-left+1)
        return result


sol = Solution()
s = "AABABBA"
k = 1
print(sol.characterReplacement(s, k))
