# Last updated: 03/11/2026, 22:39:04
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
8        counter=0
9        tempo=head
10        while tempo is not None:
11            counter+=1
12            tempo=tempo.next
13
14        if head is None:
15            return None
16        if n ==counter:
17            return head.next
18        count=0
19        temp=head
20        while temp is not None and temp.next is not None:
21            if count==(counter-n)-1:
22                temp.next=temp.next.next
23                break
24            temp=temp.next
25            count+=1
26        return head