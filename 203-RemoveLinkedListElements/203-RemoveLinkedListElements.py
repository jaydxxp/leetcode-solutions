# Last updated: 19/10/2026, 02:48:34
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode | None, val: int) -> ListNode | None:
        current= head
        prev_node=None
        while current:
            if current.val==val:
                if current==head:
                    head = current.next
                    current=head
                else:
                    prev_node.next = current.next
                    current=current.next
            else:
                prev_node=current
                current=current.next
        return head
                