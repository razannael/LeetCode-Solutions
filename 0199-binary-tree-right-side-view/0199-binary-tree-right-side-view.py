from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque()
        if root is None:
            return []
        
        if root.left is None and root.right is None:
            return [root.val]
        
        result = []
        queue.append(root)
        while queue:
            child_queue = deque()
            prev = -1
            while queue:
                curr = queue.popleft()

                if curr.left is not None:
                    child_queue.append(curr.left)

                if curr.right is not None:
                    child_queue.append(curr.right)
                
                prev = curr
            
            result.append(prev.val)
            queue = child_queue
        
        return result