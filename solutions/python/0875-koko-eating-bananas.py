"""
Problem: Koko Eating Bananas
Link: https://leetcode.com/problems/koko-eating-bananas/
Difficulty: Medium
Topics: Array, Binary Search
Time: O(n log m)
Space: O(1)
"""


import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        result = r

        while l <= r:
            m = (l + r) // 2
            t = 0
            for pile in piles:
                t += math.ceil(pile / m)

            if t <= h:
                result = min(result, m)
                r = m - 1
            else:
                l = m + 1

        return result
