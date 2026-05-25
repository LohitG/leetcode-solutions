"""
Problem: Contains Duplicate
Link: https://leetcode.com/problems/contains-duplicate/
Difficulty: Easy
Topics: Array, Hash Table, Sorting
Time: O(n)
Space: O(n)
"""


from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        from collections import defaultdict

        d = defaultdict(int)
        for num in nums:
            if d[num] != 0:
                return True
            d[num] += 1
        return False
