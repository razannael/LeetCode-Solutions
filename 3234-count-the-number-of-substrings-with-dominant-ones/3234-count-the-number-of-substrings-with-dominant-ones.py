class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        result = 0
        
        # Iterate through possible zero counts (1 to sqrt(n))
        for k in range(1, int(n**0.5) + 1):
            zeros = deque()  # Queue to store positions of zeros
            lastzero = -1    # Position of the zero before the first zero in our window
            ones = 0         # Count of ones in our current window
            
            # Scan through the string
            for right in range(n):
                if s[right] == '0':
                    zeros.append(right)
                    # If we have more than k zeros, remove the leftmost one
                    while len(zeros) > k:
                        ones -= (zeros[0] - lastzero - 1)  # Subtract ones between lastzero and the removed zero
                        lastzero = zeros.popleft()
                else:
                    ones += 1
                
                # If we have exactly k zeros and at least k^2 ones
                if len(zeros) == k and ones >= k**2:
                    # Add the minimum of:
                    # 1. Number of ways to extend to the left (zeros[0] - lastzero)
                    # 2. Number of ways to extend to the right (ones - k**2 + 1)
                    result += min(zeros[0] - lastzero, ones - k**2 + 1)
        
        # Handle all-ones substrings
        i = 0
        while i < n:
            if s[i] == '0':
                i += 1
                continue
            sz = 0
            while i < n and s[i] == '1':
                sz += 1
                i += 1
            # Add number of all-ones substrings
            result += (sz * (sz + 1)) // 2
        
        return result