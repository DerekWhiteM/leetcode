"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description

Track the lowest price seen so far.
"""

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        lowest_price = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < lowest_price:
                lowest_price = prices[i]
                continue
            profit = prices[i] - lowest_price
            if profit > max_profit:
                max_profit = profit
        return max_profit
