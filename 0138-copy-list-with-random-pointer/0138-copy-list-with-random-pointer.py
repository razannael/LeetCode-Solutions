class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hm, zero = dict(), Node(0)
        
        cur, copy = head, zero
        while cur:
            copy.next = Node(cur.val)
            hm[cur] = copy.next
            cur, copy = cur.next, copy.next
            
        cur, copy = head, zero.next
        while cur:
            copy.random = hm[cur.random] if cur.random else None
            cur, copy = cur.next, copy.next
                
        return zero.next