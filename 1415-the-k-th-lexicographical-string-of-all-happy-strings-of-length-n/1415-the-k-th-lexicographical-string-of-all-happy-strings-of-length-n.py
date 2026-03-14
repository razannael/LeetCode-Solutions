class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        # The total number of happy strings is 3 * 2^(n-1)
        # This comes from the dominant eigenvalue of the transition matrix
        total_count = 3 * (2**(n - 1))
        
        if k > total_count:
            return ""
        
        # Adjust k to be 0-indexed for easier bit-partitioning
        k -= 1
        
        # Determine the first character
        # Each block (a, b, c) has 2^(n-1) elements
        partition_size = 2**(n - 1)
        chars = ['a', 'b', 'c']
        res = [chars[k // partition_size]]
        
        # Update k to be relative to the chosen first character
        k %= partition_size
        
        # For the remaining n-1 characters, there are always 2 choices
        for i in range(n - 1, 0, -1):
            # partition_size for the next character is 2^(i-1)
            partition_size //= 2
            
            # Identify the two available characters (excluding the previous one)
            current_options = [c for c in chars if c != res[-1]]
            
            # Use the "bit" value of k to pick the option
            # If k < partition_size, pick the smaller; else pick the larger
            index = k // partition_size
            res.append(current_options[index])
            
            # Update k for the next position
            k %= partition_size
            
        return "".join(res)        