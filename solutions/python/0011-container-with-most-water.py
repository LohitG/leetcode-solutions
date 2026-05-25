"""
Problem: Container With Most Water
Link: https://leetcode.com/problems/container-with-most-water/
Difficulty: Medium
Topics: Array, Two Pointers, Greedy
Time: O(n)
Space: O(1)
"""


from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = 0
        l = 0
        r = len(height) - 1
        while l < r:
            result = max(result, (min(height[l], height[r]) * (r - l)))
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1

        return result
