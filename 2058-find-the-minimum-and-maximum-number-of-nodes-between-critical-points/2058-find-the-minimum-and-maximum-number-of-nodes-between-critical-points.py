# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev = head
        curr = head.next
        pos = 1

        first = -1
        prev_critical = -1
        min_dist = float('inf')
        max_dist = -1

        while curr.next:
            next_node = curr.next
            pos += 1

            # Check if current node is a local maximum or minimum
            if ((curr.val > prev.val and curr.val > next_node.val) or
                (curr.val < prev.val and curr.val < next_node.val)):

                if first == -1:
                    # First critical point
                    first = pos
                else:
                    # Distance from previous critical point
                    min_dist = min(min_dist, pos - prev_critical)

                    # Distance from first critical point
                    max_dist = max(max_dist, pos - first)

                prev_critical = pos

            prev = curr
            curr = next_node

        if first == -1 or prev_critical == first:
            return [-1, -1]

        return [min_dist, max_dist]      