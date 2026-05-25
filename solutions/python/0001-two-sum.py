"""
Problem: Two Sum
Link: https://leetcode.com/problems/two-sum/
Difficulty: Easy
Topics: Array, Hash Table
Time: O(n)
Space: O(n)
"""


from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        from collections import defaultdict

        d = defaultdict(int)
        for i in range(len(nums)):
            if (target - nums[i]) in d:
                return [i, d[target - nums[i]]]
            d[nums[i]] = i
        return
