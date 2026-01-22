# 3507. Minimum Pair Removal to Sort Array I
# Given an array nums, you can perform the following operation any number of times:
# Select the adjacent pair with the minimum sum in nums. If multiple such pairs exist, 
# choose the leftmost one.
# Replace the pair with their sum.
# Return the minimum number of operations needed to make the array non-decreasing.
# An array is said to be non-decreasing if each element is greater than or equal to its 
# previous element (if it exists).

class Solution(object):

    def isSort(self, t):

        for i in range(len(t) - 1):
            if (t[i] > t[i + 1]):
                return False

        return True

    def minimumPairRemoval(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        operation = 0

        while (not self.isSort(nums)):
            minSum = float('inf'); ind = -1
            
            for i in range(len(nums) - 1):
                Sum = nums[i] + nums[i + 1]

                if (Sum < minSum):
                    ind = i
                    minSum = Sum

            nums[ind] += nums[ind + 1]
            nums.pop(ind + 1)

            operation += 1

        return operation