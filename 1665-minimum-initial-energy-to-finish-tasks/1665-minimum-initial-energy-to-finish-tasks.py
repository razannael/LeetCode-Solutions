class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        # Sort by the "buffer" requirement (minimum - actual) descending
        # This is our exchange-argument based greedy strategy
        tasks.sort(key=lambda x: x[1] - x[0], reverse=True)
        
        current_energy = 0
        total_needed = 0
        
        for actual, minimum in tasks:
            # If current energy is less than the requirement, 
            # we must have started with more.
            if current_energy < minimum:
                total_needed += (minimum - current_energy)
                current_energy = minimum
            
            # Spend the energy
            current_energy -= actual
            
        return total_needed        