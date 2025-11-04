class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        rand49 = float('inf')
        while rand49 >= 40:
            rand49 = 7 * (rand7() - 1) + (rand7() - 1)
        # Since rand49 % 10 => [0, 9] and the output has to be in range [1,10]
        return rand49 % 10 + 1 