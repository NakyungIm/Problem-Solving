# https://leetcode.com/problems/valid-palindrome/description/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r"[^\uAC00-\uD7A30-9a-zA-Z\s]", "", s).lower()
        s = s.replace(" ", "")
        n = len(s)
        for i in range(0, int(n/2)):
            if s[i] != s[n-1-i]:
                return False
            else:
                pass
        return True