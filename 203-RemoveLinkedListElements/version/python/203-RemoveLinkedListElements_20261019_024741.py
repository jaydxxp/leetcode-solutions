# Last updated: 19/10/2026, 02:47:41
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def removeElements(self, head: ListNode | None, val: int) -> ListNode | None:
8        current= head
9        prev_node=None
10        while current:
11            if current.val==val:
12                if current==head:
13                    head = current.next
14                    current=head
15                else:
16                    prev_node.next = current.next
17                    current=current.next
18            else:
19                prev_node=current
20                current=current.next
21        return head
22                