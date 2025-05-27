class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        stackA = ['A']
        stackB = ['B']

        while headA or headB:
            if headA:
                stackA.append(headA)
                headA = headA.next

            if headB:
                stackB.append(headB)
                headB = headB.next

        prev = None
        while stackA and stackB:
            nodeA = stackA.pop(-1)
            nodeB = stackB.pop(-1)

            if nodeA != nodeB:
                return prev

            prev = nodeA