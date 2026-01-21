# https://leetcode.com/problems/valid-parentheses/description/

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')':'(', '}':'{', ']':'['}

        for i in s:
            if i in mapping: # close bracket
                if len(stack) == 0 or stack[-1] != mapping[i]:
                    return False
                stack.pop()
            else: stack.append(i) # open bracket
        return len(stack) == 0
        