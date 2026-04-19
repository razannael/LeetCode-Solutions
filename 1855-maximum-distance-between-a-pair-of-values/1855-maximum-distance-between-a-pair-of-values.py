import numpy as np

class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        n1 = np.array(nums1)
        n2 = np.array(nums2)
        
        # 1. Finite Difference Operator
        # We find the indices where the value actually changes in nums2
        # This reduces the search manifold to only the 'step' points.
        diffs = np.diff(n2)
        change_indices = np.where(diffs != 0)[0]
        
        # Append the last index to complete the manifold
        support_points = np.append(change_indices, len(n2) - 1)
        
        # 2. Sparse Basis Search
        # Instead of searching the full n2, we search the sparse support manifold
        sparse_n2_neg = -n2[support_points]
        n1_neg = -n1
        
        # Vectorized search on the sparse manifold
        sparse_j_indices = np.searchsorted(sparse_n2_neg, n1_neg, side='right') - 1
        
        # Map back from sparse indices to the original coordinate manifold
        # If j_idx is -1 (no match), we handle it by filtering later
        valid_mask = sparse_j_indices >= 0
        j_coords = np.full(len(n1), -1)
        j_coords[valid_mask] = support_points[sparse_j_indices[valid_mask]]
        
        # 3. Maximum Shift Calculation
        i_coords = np.arange(len(n1))
        distances = j_coords - i_coords
        
        return int(np.max(distances, initial=0))        