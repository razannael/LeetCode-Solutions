class Solution:
    def isOneBitCharacter(self, bits):
        n = len(bits)
        currIndex = 0

        # If the last bit is 1, it can't possibly be a single-bit "0"
        if bits[-1] == 1:
            return False

        while currIndex < n:
            if bits[currIndex] == 0:
                # A leading 0 always means a one-bit character
                # If this 0 is the last element, then the last character IS "0"
                if currIndex == n - 1:
                    return True
                currIndex += 1  # move forward by 1
            else:
                # A leading 1 always means a two-bit character ("10" or "11")
                currIndex += 2  # skip both bits

        # If we never returned true, the last character was part of a two-bit code
        return False