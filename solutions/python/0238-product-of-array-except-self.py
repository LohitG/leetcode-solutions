"""
Problem: Product of Array Except Self
Link: https://leetcode.com/problems/product-of-array-except-self/
Difficulty: Medium
Topics: Array, Prefix Sum
Time: O(n)
Space: O(n)
"""


from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = list(nums)
        postfix = list(nums)
        for i in range(1, len(prefix)):
            prefix[i] = prefix[i] * prefix[i - 1]

        for i in range(len(postfix) - 2, 0, -1):
            postfix[i] = postfix[i] * postfix[i + 1]

        result = []
        for i in range(len(nums)):
            temp = 1
            if i - 1 >= 0:
                temp = temp * prefix[i - 1]
            if i + 1 < len(nums):
                temp = temp * postfix[i + 1]
            result.append(temp)

        return result
