class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        #Initialize sets for cols, diag1, diag2. Later, Diag1 will store (r + c) values and Diag2 will store (r - c) values. This is to handle two different types of diagonals
        cols = set()
        diag1 = set()
        diag2 = set()

        #Intialize empty output array res
        res = []
        #Initialize board to [["."] * n for i in range(n)]
        board = [["."] * n for i in range(n)]

        #create helper function backtrack that takes r as a pameter
        def backtrack(r):
            #Check if r is already equal to n
            if r == n:
                #Initialize copy to ["".join(row) for row in board]
                copy = ["".join(row) for row in board]
                #append copy to res
                res.append(copy)
                #return as r is already eqqual to n
                return

            #Iterate in range n for c
            for c in range(n):
                #Check if c in cols or (r + c) in diag1 or (r - c) in diag2
                if c in cols or (r + c) in diag1 or (r - c) in diag2:
                    #skip and continue
                    continue

                #Add c to cols set
                cols.add(c)
                #Add r + c to diag1 set
                diag1.add(r + c)
                #Add r - c to diag2 set
                diag2.add(r - c)
                #Update value in board[r][c] array to "Q"
                board[r][c] = "Q"

                #Call backtrack by passing r + 1 to it
                backtrack(r + 1)
                
                #Remove c from cols set
                cols.remove(c)
                #Remove r + c from diag1 set
                diag1.remove(r + c)
                #Remove r - c from diag2 set
                diag2.remove(r - c)
                #Update value in board[r][c] array to "."
                board[r][c] = "."

        #Call backtrack() by passing 0 as parameter
        backtrack(0)
        #return res
        return res
        