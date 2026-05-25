"""
Problem: Top K Frequent Elements
Link: https://leetcode.com/problems/top-k-frequent-elements/
Difficulty: Medium
Topics: Array, Hash Table, Divide and Conquer, Sorting, Heap, Bucket Sort, Counting
Time: O(n)
Space: O(n)
"""


from collections import defaultdict
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for num in nums:
            d[num] += 1

        freq = [[] for i in range(len(nums) + 1)]

        for key, value in d.items():
            freq[value].append(key)

        result = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                result.append(num)
            if len(result) == k:
                return result

        return result
