# Last updated: 19/10/2026, 02:39:22
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def removeElements(self, head: ListNode | None, val: int) -> ListNode | None:
8        dummy_head = ListNode(-1)
9        dummy_head.next = head
10        
11        current_node = dummy_head
12        while current_node.next != None:
13            if current_node.next.val == val:
14                current_node.next = current_node.next.next
15            else:
16                current_node = current_node.next
17                
18        return dummy_head.next
19                