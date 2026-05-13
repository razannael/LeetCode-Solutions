from itertools import accumulate

class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        # We treat 'line' as the discrete derivative of the Cost Function
        line = [0] * (2 * limit + 2)
        
        for i in range(n // 2):
            a, b = nums[i], nums[n - 1 - i]
            if a > b: a, b = b, a
            
            # Instead of procedural updates, think of these as 
            # Boundary Conditions for our piece-wise linear function.
            # We add 'mass' to the derivative at specific transition points.
            line[2] += 2
            line[a + 1] -= 1
            line[a + b] -= 1
            line[a + b + 1] += 1
            line[b + limit + 1] += 1
            
        # The Cost Function C(S) is the Prefix Sum (Integral) of our 'line'.
        # We find the global minimum of this reconstructed waveform.
        # This is the discrete equivalent of finding min( integral( f'(x) dx ) )
        return min(accumulate(line[2 : 2 * limit + 1]))   