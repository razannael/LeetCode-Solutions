# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #Solution 2 Optimal
        n = 0
        crrNode = head
        oldtail = crrNode
        while crrNode is not None:
            n+=1
            oldtail = crrNode
            crrNode = crrNode.next
        oldhead = head
        
        if n<2:
            return head

        k=k%n
        if k==0:
            return head

        crrNode = head
        for _ in range(n-k-1):
            crrNode = crrNode.next
        newtail = crrNode
        newhead = newtail.next
        oldtail.next = oldhead
        newtail.next = None

        return newhead