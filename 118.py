# 118. Pascal's Triangle
# Given an integer numRows, return the first numRows of Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly 


class Solution:
    def generate(self, numRows):
        arr = []
        for i in range(numRows):
            row = [0] * (i + 1)
            arr.append(row)
            for j in range(i + 1):
                if j == 0 or j == i:
                    arr[i][j] = 1
                else:
                    arr[i][j] = arr[i - 1][j] + arr[i - 1][j - 1]
        return arr