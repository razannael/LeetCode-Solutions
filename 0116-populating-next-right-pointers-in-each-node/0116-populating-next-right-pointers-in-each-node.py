class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return None

        leftmost = root

        while leftmost.left:
            cur = leftmost

            while cur:
                cur.left.next = cur.right

                if cur.next:
                    cur.right.next = cur.next.left

                cur = cur.next

            leftmost = leftmost.left

        return root