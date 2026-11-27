class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        """
        Solves the mini-max optimization problem using prefix mass tracking
        and exact integer ceiling boundaries.
        """
        global_max_peak = 0
        prefix_mass_sum = 0
        
        # Sequentially evaluate the capacity limits of each prefix window
        for i, val in enumerate(nums):
            prefix_mass_sum += val
            
            # Mathematical optimization: Find the ceiling of the uniform distribution average
            # using exact integer arithmetic to prevent floating-point precision drift.
            current_prefix_bound = (prefix_mass_sum + i) // (i + 1)
            
            # The global maximum must accommodate the most constrained prefix window
            if current_prefix_bound > global_max_peak:
                global_max_peak = current_prefix_bound
                
        return global_max_peak        