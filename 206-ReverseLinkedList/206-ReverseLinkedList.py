# Last updated: 20/10/2026, 23:59:53
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        prev=None
        current=head
        nextt=None
        while(current!=None):
            nextt=current.next
            current.next=prev
            prev=current
            current=nextt
        return prev