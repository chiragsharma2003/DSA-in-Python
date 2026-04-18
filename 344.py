# 344. Reverse String
# Write a function that reverses a string. The input string is given as an array
# of characters s. You must do this by modifying the input array in-place with
# O(1) extra memory.

class Solution(object):
    def reverseString(self, s):
        # Two pointers, i pointing to the start and j pointing to the end of the list
        i = 0
        j = len(s) - 1

        while i < j:
            # Swap the characters at positions i and j
            s[i], s[j] = s[j], s[i]

            # Move i one step forward and j one step backward
            i += 1
            j -= 1