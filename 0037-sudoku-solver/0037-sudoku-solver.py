class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = [set() for _ in range(9)] # numbers used in row
        cols = [set() for _ in range(9)] # numbers used in col
        grids = [[set() for _ in range(3)] for _ in range(3)] # numbers used in grid
        empty_cells = []
        for i, row in enumerate(board): # collect numbers and add empty cells
            for j, value in enumerate(row):
                if value == ".": # found empty cell
                    empty_cells.append((i, j))
                else: # found number
                    rows[i].add(value)
                    cols[j].add(value)
                    grids[i//3][j//3].add(value)                     

        # [ (potential numbers for cell), i, j] 
        empty_cells = [
            (9 - len(rows[i] | cols[j] | grids[i//3][j//3]), i, j)
            for i, j in empty_cells
        ]
        heapq.heapify(empty_cells) # sort by lowest potential numbers for cell

        def fill_board():
            if not empty_cells: 
                return True # finished filling board

            _, i, j = heapq.heappop(empty_cells)
            row = rows[i]
            col = cols[j]
            grid = grids[i//3][j//3]
            potential_nums = 0  
            for value in '123456789': # check possible numbers for each cell
                if (value in row or value in col or value in grid): 
                    continue # skip if number present in row, col, or grid

                board[i][j] = value # add number to board and row / col / grid
                row.add(value)
                col.add(value)
                grid.add(value)

                if fill_board(): # try to fill in rest of board
                    return True

                row.remove(value) # couldn't fill rest of board, take out used number
                col.remove(value)
                grid.remove(value)
                potential_nums += 1 # didn't use value, add another option for cell

            heapq.heappush(empty_cells, (potential_nums, i, j)) # didn't fill cell, add back to empty cells
            return False
            
        fill_board()