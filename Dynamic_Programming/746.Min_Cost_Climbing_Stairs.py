# https://leetcode.com/problems/min-cost-climbing-stairs/

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        f = [0, 0]
        if n <= 1: return f[n]
        for i in range(2, n+1):
            f.append(min(f[i-1]+cost[i-1], f[i-2]+cost[i-2]))
        return f[n]