class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:        
        N = len(grid)

        @cache
        def maxPath(i: int, j: int, I: int, J: int) -> int:
            # one of the warriors/both warriors got lost, or ended up at a thorn
            if  (i < 0 or N <= i or j < 0 or N <= j or grid[i][j]==-1) or \
                (I < 0 or N <= I or J < 0 or N <= J or grid[I][J]==-1):
                return -math.inf
            
            # both warriors meet at N-1, N-1
            if i == N-1 and j == N-1 and I == N-1 and J == N-1: return grid[i][j]
            
            return (grid[i][j] if i==I and j==J else grid[i][j] + grid[I][J]) + max(
                maxPath( i+1, j, I+1, J ),          # both warriors go bottom
                maxPath( i, j+1, I, J+1 ),          # both warriors go right
                maxPath( i, j+1, I+1, J ),          # 1 goes right and 2 goes bottom
                maxPath( i+1, j, I, J+1 ),          # 1 goes bottom and 2 goes right
            )

        return max(0, maxPath(0, 0, 0, 0))