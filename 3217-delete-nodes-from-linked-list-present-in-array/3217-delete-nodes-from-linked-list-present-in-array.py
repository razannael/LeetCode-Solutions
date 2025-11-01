class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def modifiedList(self, nums, head: ListNode) -> ListNode:
        # Convert nums to a set for O(1) lookups
        to_delete = set(nums)
        
        # Create a dummy node that points to the head of the list
        dummy = ListNode(0)
        dummy.next = head
        
        # Use two pointers: current to iterate and prev to manage the deletion
        prev = dummy
        current = head
        
        while current:
            if current.val in to_delete:
                # Skip the node to be deleted
                prev.next = current.next
            else:
                # Move prev to current
                prev = current
            
            # Move to the next node
            current = current.next
        
        # Return the modified list, which is next of dummy
        return dummy.next