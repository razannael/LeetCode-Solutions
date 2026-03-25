from typing import List

class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        # Calculate total grid sum
        total_sum = sum(sum(row) for row in grid)
        
        # If the total sum is odd, return False
        if total_sum % 2 != 0:
            return False
        
        target_sum = total_sum // 2
        
        # Check horizontal cuts
        row_sum = 0
        for i in range(len(grid) - 1):
            row_sum += sum(grid[i])
            if row_sum == target_sum:
                return True
        
        # Check vertical cuts
        col_sums = [0] * len(grid[0])
        for row in grid:
            for j in range(len(row)):
                col_sums[j] += row[j]
        
        col_sum = 0
        for j in range(len(col_sums) - 1):
            col_sum += col_sums[j]
            if col_sum == target_sum:
                return True
        
        return False
