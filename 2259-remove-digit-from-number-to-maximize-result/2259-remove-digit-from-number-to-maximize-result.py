class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        res = ""
        
        for i in range(len(number)):
            if number[i] == digit:
                # Try removing digit at index i and compare results
                new_number = number[:i] + number[i+1:]
                res = max(res, new_number)  # Keep the max lexicographically
                
        return res
