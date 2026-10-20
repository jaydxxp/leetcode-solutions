# Last updated: 21/10/2026, 00:21:17
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def middleNode(self, head: ListNode | None) -> ListNode | None:
8        slow=head
9        fast=head
10        while fast is not None and fast.next is not None:
11            slow=slow.next
12            fast=fast.next.next
13        return slow