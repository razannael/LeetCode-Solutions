class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        
        board.reverse()                                     #  <–– convert the board to 1D list
        for i in range(1,len(board),2): board[i].reverse()
        arr = [None]+list(chain(*board))                    #  <–– add an initial element (None) 
                                                            #      to make indexing simpler
                                                            
        n, queue, seen, ct = len(arr)-1, deque([1]), {1}, 0               

        while queue:                                        #  <–– BFS search for arr[n]
            lenQ = len(queue)

            for _ in range(lenQ):                           #  <–– one level of BFS

                cur = queue.popleft()
                if cur == n: return ct

                for i in range(cur+1, min(cur+7,n+1)):      #  <–– iterate through the possible next moves
                    nxt = arr[i] if arr[i]+1 else i         #  <–– determine whether snake or ladder

                    if nxt in seen: continue                #  <–– avoid revisiting positions        
                    seen.add(nxt)
                    queue.append(nxt)                       #  <–– build queue for next level
                    
            ct += 1                    
        
        return -1