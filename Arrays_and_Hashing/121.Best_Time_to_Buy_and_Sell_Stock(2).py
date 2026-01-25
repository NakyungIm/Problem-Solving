# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy_price = prices[0]

        for i in prices[1:]:
            if buy_price > i:
                buy_price = i
            profit = max(profit, i - buy_price)
        return profit
        