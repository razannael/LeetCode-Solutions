from collections import deque


class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])

        layers = min(m, n) // 2  # each layer requires two rows and two columns

        for layer in range(layers):
            nums = []

            top = layer
            bottom = m - layer - 1
            left = layer
            right = n - layer - 1

            # Top row (left -> right)
            for j in range(left, right + 1):
                nums.append(grid[top][j])

            # Right column (top -> bottom)
            for i in range(top + 1, bottom):
                nums.append(grid[i][right])

            # Bottom row (right -> left)
            for j in range(right, left - 1, -1):
                nums.append(grid[bottom][j])

            # Left column (bottom -> top)
            for i in range(bottom - 1, top, -1):
                nums.append(grid[i][left])

            length = len(nums)
            normalized_k = k % length

            # Rotate the list to the left by normalized_k
            d = deque(nums)
            d.rotate(-normalized_k)
            nums = list(d)

            idx = 0

            for j in range(left, right + 1):
                grid[top][j] = nums[idx]
                idx += 1

            for i in range(top + 1, bottom):
                grid[i][right] = nums[idx]
                idx += 1

            for j in range(right, left - 1, -1):
                grid[bottom][j] = nums[idx]
                idx += 1

            for i in range(bottom - 1, top, -1):
                grid[i][left] = nums[idx]
                idx += 1

        return grid