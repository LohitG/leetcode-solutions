"""
Problem: Valid Palindrome
Link: https://leetcode.com/problems/valid-palindrome/
Difficulty: Easy
Topics: Two Pointers, String
Time: O(n)
Space: O(n)
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(c.lower() for c in s if c.isalnum())
        l = 0
        r = len(s) - 1

        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1

        return True
