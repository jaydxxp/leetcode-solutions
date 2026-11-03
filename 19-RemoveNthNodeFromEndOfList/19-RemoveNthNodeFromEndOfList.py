# Last updated: 03/11/2026, 22:40:09
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        counter=0
        tempo=head
        while tempo is not None:
            counter+=1
            tempo=tempo.next

        if head is None:
            return None
        if n ==counter:
            return head.next
        count=0
        temp=head
        while temp is not None and temp.next is not None:
            if count==(counter-n)-1:
                temp.next=temp.next.next
                break
            temp=temp.next
            count+=1
        return head