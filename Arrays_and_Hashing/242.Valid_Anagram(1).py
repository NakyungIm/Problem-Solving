# https://leetcode.com/problems/valid-anagram/
# String

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        for i in range(len(t)):
            if t[i] in s:
                s = s[0:s.index(t[i])] + s[s.index(t[i])+1: len(s)]
            else: pass
        
        if s == "": return True
        else: return False
        