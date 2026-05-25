"""
Problem: Valid Anagram
Link: https://leetcode.com/problems/valid-anagram/
Difficulty: Easy
Topics: Hash Table, String, Sorting
Time: O(n + m)
Space: O(1)
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import defaultdict

        d = defaultdict(int)
        for l in s:
            d[l] += 1

        for l in t:
            d[l] -= 1

        for key in d:
            if d[key] != 0:
                return False

        return True
