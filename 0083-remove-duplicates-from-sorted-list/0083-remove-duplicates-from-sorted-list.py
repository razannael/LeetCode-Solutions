
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        mov: ListNode = head

        while mov is not None and mov.next is not None:
            if mov.val == mov.next.val:
                mov.next = mov.next.next
            else:
                mov = mov.next

        return head 