"""
Problem: Binary Search
Link: https://leetcode.com/problems/binary-search/
Difficulty: Easy
Topics: Array, Binary Search
Time: O(log n)
Space: O(1)
"""


from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (r + l) // 2
            if target < nums[m]:
                r = m - 1
            elif target == nums[m]:
                return m
            else:
                l = m + 1

        return -1
