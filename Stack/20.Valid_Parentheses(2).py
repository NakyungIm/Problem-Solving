# https://leetcode.com/problems/valid-parentheses/description/

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {')':'(', '}':'{', ']':'['}
        
        for i in s:
            if i in brackets: # if i is in bracket keys
                if stack == 0 or stack[-1] != brackets[i]: # if stack is empty or last element in stack is not equal to (, {, [
                    return False
                else: # brackets are matched
                    stack.pop()
            else: # if is is not in bracket keys
                stack.append(i)
        return len(stack) == 0