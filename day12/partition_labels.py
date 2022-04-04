from collections import defaultdict


class Solution:
    def partitionLabels(self, s: str):
        indexes = defaultdict(list)
        size = len(s)
        if size == 1:
            return [1]

        for i in range(size):
            if s[i] not in indexes or len(indexes[s[i]]) < 2:
                indexes[s[i]].append(i)
            else:
                indexes[s[i]][-1] = i

        left = indexes[s[0]][0]
        right = indexes[s[0]][-1]
        result = []
        while left < size and right < size:
            count = 0
            while left < size and right < size:
                right = max(right, indexes[s[left]][-1])
                count += 1
                if left == right:
                    break
                left += 1

            if count == 0:
                right += 1
            else:
                result.append(count)
            left += 1
        return result


sol = Solution()
print(sol.partitionLabels("ababcbacadefegdehijhklij"))
