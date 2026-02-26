# https://leetcode.com/problems/longest-palindrome/

class Solution:
    def longestPalindrome(self, s: str) -> int:
        hashmap = {}
        for l in s:
            if l in hashmap:
                hashmap[l] += 1
            else: hashmap[l] = 1

        res = 0
        has_odd = False

        for v in hashmap.values():
            if v%2 != 0: # If num is not evenly divisible by 2 (Odd number)
                res += v-1
                has_odd = True
            else: # If num is evenly divisible by 2 (Even number)
                res += v

        if has_odd == True:
            res += 1

        return res