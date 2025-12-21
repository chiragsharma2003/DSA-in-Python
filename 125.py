# A phrase is a palindrome if, after converting all uppercase letters into lowercase 
# letters and removing all non-alphanumeric characters, it reads the same forward and 
# backward. Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.

class Solution(object):
    def isPalindrome(self, s):
        new = []
        for i in s:
            if i.isalnum():
                new.append(i.lower())
        return new == new[::-1]