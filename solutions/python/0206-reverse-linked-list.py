"""
Problem: Reverse Linked List
Link: https://leetcode.com/problems/reverse-linked-list/
Difficulty: Easy
Topics: Linked List, Recursion
Time: O(n)
Space: O(1)
"""


from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp

        return prev
