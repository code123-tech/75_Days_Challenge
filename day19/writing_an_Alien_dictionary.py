class Solution:
    def isAlienSorted(self, words, order) -> bool:

        def compare(w1, w2):
            i, j = 0, 0
            while i < len(w1) and j < len(w2) and w1[i] == w2[j]:
                i += 1
                j += 1
            if i == len(w1) and j == len(w2):
                return True
            if i == len(w1) and j < len(w2):
                return True
            if i < len(w1) and j == len(w2):
                return False
            if i < len(w1) and j < len(w2):
                return True if order.index(w1[i]) <= order.index(w2[j]) else False

        for i in range(len(words)-1):
            if not compare(words[i], words[i+1]):
                return False
        return True


sol = Solution()
words = ["hello", "leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"
print(sol.isAlienSorted(words, order))
