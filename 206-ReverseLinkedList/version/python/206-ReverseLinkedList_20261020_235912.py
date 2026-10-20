# Last updated: 20/10/2026, 23:59:12
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def reverseList(self, head: ListNode | None) -> ListNode | None:
8        prev=None
9        current=head
10        nextt=None
11        while(current!=None):
12            nextt=current.next
13            current.next=prev
14            prev=current
15            current=nextt
16        return prev