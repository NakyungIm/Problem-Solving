# https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        step = [1, 2]
        if n <= 2:
            return step[n-1]
        else:
            for i in range(2, n):
                step.append(step[i-1] + step[i-2])
        return step[n-1]