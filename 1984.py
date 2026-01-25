# 1984. Minimum Difference Between Highest and Lowest of K Scores
# You are given a 0-indexed integer array nums, where nums[i] represents the 
# score of the ith student. You are also given an integer k.
# Pick the scores of any k students from the array so that the difference 
# between the highest and the lowest of the k scores is minimized.
# Return the minimum possible difference.

class Solution(object):
    def minimumDifference(self, nums, k):
        if k == 1:
            return 0
        diff = float('inf')
        n = len(nums)
        nums.sort()
        left = 0
        right = k-1
        while right < n:
            diff = min(diff, nums[right] - nums[left])
            right += 1
            left += 1
        return diff