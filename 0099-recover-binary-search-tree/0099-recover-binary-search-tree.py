def recoverTree(self, root: Optional[TreeNode]) -> None:
       
        res = []     
        startnode = None
        prev = None
        lastnode = None
        
        def dfs(root):
            nonlocal res, startnode, prev, lastnode
            if not root:
                return 
            # go to left  (inorder step 1)  
            dfs(root.left)
			
            # do processing....(inorder step 2)
			# get the first node where the sorted order is broken the first time and the last time
            if prev and prev.val > root.val:
                if not startnode:
                    startnode = prev
                lastnode = root
                
            prev = root
			
            # go to right (inorder step 3)    
            dfs(root.right)
            
        
        dfs(root)
        # swap the nodes that are not in place
        if startnode and lastnode:
            startnode.val, lastnode.val = lastnode.val, startnode.val