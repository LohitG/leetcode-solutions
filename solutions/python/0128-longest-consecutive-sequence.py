"""
Problem: Longest Consecutive Sequence
Link: https://leetcode.com/problems/longest-consecutive-sequence/
Difficulty: Medium
Topics: Array, Hash Table, Union Find
Time: O(n)
Space: O(n)
"""


from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        result = 1

        if len(nums) == 0:
            return 0

        for num in s:
            temp = 1
            if (num - 1) not in s:
                while (num + 1) in s:
                    temp += 1
                    num += 1

                result = max(result, temp)

        return result
