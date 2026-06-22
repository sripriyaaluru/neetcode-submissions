# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #floyd's algorithm
        slow, fast=head,head
        while fast and fast.next: #to access fast.next.next, fats.next must exist, similarly with fast must exist for fast.next
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return True
        return False
            
        