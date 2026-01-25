# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        min_v = prices[0]
        max_profit = 0
        for i in range(len(prices)):
            if min_v >= prices[i]:
                min_v = prices[i]
            else:
                max_profit = max(max_profit, prices[i]-min_v)
        return max_profit
