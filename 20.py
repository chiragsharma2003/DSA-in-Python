# 20. Valid Parentheses 
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
# determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

class Solution(object):
    def isValid(self, s):
        # inp = "){"
        stack=[]
        dicts = { ")":"(", "}":"{", "]":"["} #.get(key), dicts["key"]
        if (len(s)==1):
            return False
        for x in range(len(s)):#len= 3
            if s[x] in "({[": # 
                stack.append(s[x])
            elif s[x] in "}])" and stack: #
                if stack[-1] == dicts[s[x]]: #it is false
                    stack.pop()#
                else:
                    return False 
            # case for when stack is empty, and and s[x] an enlosed bracket
            else:
                return False

        return not stack #len(stack)==0