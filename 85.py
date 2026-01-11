# 85. Maximal Rectangle
# Given a rows x cols binary matrix filled with 0's and 1's, find the largest
# rectangle containing only 1's and return its area.

class Solution:
    def maximalRectangle(self, matrix):
        if not matrix: return 0
        n = len(matrix[0])
        height = [0]*n
        ans = 0

        for row in matrix:
            for i in range(n):
                height[i] = height[i] + 1 if row[i] == '1' else 0
            stack = []
            for i in range(n+1):
                cur = height[i] if i < n else 0
                while stack and height[stack[-1]] > cur:
                    h = height[stack.pop()]
                    w = i if not stack else i - stack[-1] - 1
                    ans = max(ans, h*w)
                stack.append(i)
        return ans