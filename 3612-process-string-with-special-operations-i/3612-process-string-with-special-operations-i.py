class Solution:
    """
        Processes a string based on specific character commands:
        - Lowercase letters: Added to the result.
        - '*': Removes the last element (Backspace functionality).
        - '#': Duplicates the current result set.
        - '%': Reverses the current result set.
        
        Complexity Analysis:
        - Time: O(N * K), where N is the number of characters and K 
          is the length of the list during '%' or '#' operations.
        - Space: O(N) to store the result list.
        """
    def processStr(self, s: str) -> str:
        result = []

        for c in s:
            if c.islower():
                result.append(c)
            elif c == '*':
                if result:
                    result.pop()
            elif c == '#':
                # Production note, this was the fastest way to do the doubling of the string
                result += result 

                # Production note: Using the built-in .reverse() method
                # is the most efficient 'best practice' way to perform
                # an in-place reversal in Python.
            elif c == '%':
                result.reverse()
        
        return "".join(result)