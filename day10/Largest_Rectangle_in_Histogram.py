class Solution:
    def largestRectangleArea(self, heights):
        stack = list()
        index = 0
        max_area = 0
        while index < len(heights):
            if (not stack) or heights[stack[-1]] <= heights[index]:
                stack.append(index)
                index += 1
            else:
                top = stack.pop()
                area = (heights[top]*((index-stack[-1]-1) if stack else index))
                max_area = max(max_area, area)
        while stack:
            top = stack.pop()
            area = (heights[top]*((index-stack[-1]-1) if stack else index))
            max_area = max(max_area, area)
        return max_area


sol = Solution()
heights = [2, 1, 5, 6, 2, 3]
print(sol.largestRectangleArea(heights))

'''
heights = [2, 1, 5, 6, 2, 3]



'''
