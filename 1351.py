# 1351. Count Negative Numbers in a Sorted Matrix
# Given a m x n matrix grid which is sorted in non-increasing order both row-wise and 
# column-wise, return the number of negative numbers in grid.


class Solution(object):
        def countNegatives(self, grid):
            return sum(a<0 for i in grid for a in i)
        