class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        
        def nextDay(cells):
            mask = cells.copy()
            for i in range(1, len(cells) - 1):
                if mask[i-1] ^ mask[i+1] == 0:
                    cells[i] = 1
                else:
                    cells[i] = 0
            cells[0] = 0
            cells[-1] = 0   
            return cells
        
        day1 = tuple(nextDay(cells))
        N -= 1
        count = 0
        
        while N > 0:
            day = tuple(nextDay(cells))
            N -= 1
            count += 1
            
            if day == day1:
                N = N % count
        return cells
            
                
    