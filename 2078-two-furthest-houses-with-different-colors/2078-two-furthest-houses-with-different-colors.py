import numpy as np

class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        c = np.array(colors)
        n = len(c)
        
        # Scenario 1: Compare everything to the first house (index 0)
        # Create a boolean mask where the color is NOT the same as the first house
        mask_from_start = c != c[0]
        
        # Get the indices where the mask is True
        # np.where returns a tuple of arrays; we take the first one [0]
        diff_indices_start = np.where(mask_from_start)[0]
        
        # The furthest house from the start is the last index in this list
        dist1 = diff_indices_start[-1] if diff_indices_start.size > 0 else 0
        
        # Scenario 2: Compare everything to the last house (index n-1)
        mask_from_end = c != c[-1]
        diff_indices_end = np.where(mask_from_end)[0]
        
        # The furthest house from the end is (n - 1) - (the first index in this list)
        dist2 = (n - 1) - diff_indices_end[0] if diff_indices_end.size > 0 else 0
        
        return int(max(dist1, dist2))        