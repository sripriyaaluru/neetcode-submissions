# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        start = ListNode()
        curr = start

        a = list1
        b = list2

        while a and b:
            if a.val <= b.val:
                curr.next = a
                a = a.next
            else:
                curr.next = b
                b = b.next
            curr = curr.next

        if a:
            curr.next = a
        else:
            curr.next = b

        return start.next
        