class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        #summarizing row into number 
        row = [0]*m 
        for i in range(m):
            row[i] = next((j for j in reversed(range(n)) if grid[i][j]), 0)
        
        ans = 0
        #sequentially looking for row to fill in 
        for k in range(m): 
            for i, v in enumerate(row): 
                if v <= k: #enough trailing zeros 
                    ans += i
                    row.pop(i) #value used 
                    break 
            else: return -1 #cannot find such row 
        return ans 