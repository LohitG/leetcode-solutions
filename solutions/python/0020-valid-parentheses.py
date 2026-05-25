"""
Problem: Valid Parentheses
Link: https://leetcode.com/problems/valid-parentheses/
Difficulty: Easy
Topics: String, Stack
Time: O(n)
Space: O(n)
"""


from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        d = {")": "(", "]": "[", "}": "{"}

        for c in s:
            if c not in d:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                if d[c] != stack.pop():
                    return False

        return len(stack) == 0
