# 3314. Construct the Minimum Bitwise Array I
# You are given an array nums consisting of n prime integers.
# You need to construct an array ans of length n, such that, for each index i, the 
# bitwise OR of ans[i] and ans[i] + 1 is equal to nums[i], 
# i.e. ans[i] OR (ans[i] + 1) == nums[i].
# Additionally, you must minimize each value of ans[i] in the resulting array.
# If it is not possible to find such a value for ans[i] that satisfies the condition, 
# then set ans[i] = -1.

class Solution(object):
    def minBitwiseArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []

        for num in nums:
            found = -1
            for x in range(num):
                if (x | (x + 1)) == num:
                    found = x
                    break
            ans.append(found)

        return ans