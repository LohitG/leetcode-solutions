"""
Problem: Group Anagrams
Link: https://leetcode.com/problems/group-anagrams/
Difficulty: Medium
Topics: Array, Hash Table, String, Sorting
Time: O(n * k)
Space: O(n * k)
"""


from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] += 1
            d[tuple(count)].append(s)

        return list(d.values())
