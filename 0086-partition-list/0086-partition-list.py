# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        before = ListNode()
        after = ListNode()
        bTrail = before
        aTrail = after
        while head:
            if head.val < x :
                bTrail.next = head
                bTrail = bTrail.next
            else:
                aTrail.next = head
                aTrail = aTrail.next
            head = head.next
        bTrail.next = after.next
        aTrail.next = None
        return before.next