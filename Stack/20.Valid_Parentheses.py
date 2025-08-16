# https://leetcode.com/problems/valid-parentheses/description/

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if len(stack)==0 and s[i]in (')', '}', ']'):
                return False
            if s[i] in ('(', '{', '['):
                stack.append(s[i])
            elif s[i]==')' and stack[-1]=='(':
                stack.pop()
            elif s[i]=='}' and stack[-1]=='{':
                stack.pop()
            elif s[i]==']' and stack[-1]=='[':
                stack.pop()
            else:
                stack.append(s[i])
        if len(stack)==0: return True
        else: return False

