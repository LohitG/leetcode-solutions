"""
Problem: Best Time to Buy and Sell Stock
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
Difficulty: Easy
Topics: Array, Dynamic Programming
Time: O(n)
Space: O(1)
"""


from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1

        if len(prices) < 2:
            return 0

        profit = max(0, prices[r] - prices[l])

        while r < len(prices):
            if prices[r] >= prices[l]:
                profit = max(profit, prices[r] - prices[l])
            else:
                l = r
            r += 1

        return profit
