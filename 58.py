# 58. Length of Last Word
# Given a string s consisting of words and spaces, return the length of the 
# last word in the string.
# A word is a maximal substring consisting of non-space characters only.

class Solution(object):
    def lengthOfLastWord(self, s):
        l = []
        count = 0
        for i in s:
            if i != ' ':
                count += 1
            else:
                if count != 0:
                    l.append(count)
                    count = 0

        if count != 0:
            l.append(count)
        return l[-1] if l else 0