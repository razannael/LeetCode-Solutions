class Solution:
    def numSubmatrixSumTarget(self, matrix, target):
        # Get the number of rows and columns of the matrix
        m = len(matrix)
        n = len(matrix[0])
        # Initialize the answer to zero
        ans = 0
        # Loop through each row
        for i in range(m):
            # Initialize a list to store the column sums
            col = [0] * n
            # Loop through each row from i to m
            for j in range(i, m):
                # Loop through each column
                for k in range(n):
                    col[k] += matrix[j][k]
                ans += self.f(col, target)
        return ans

    # Define a helper method that takes a list of numbers and a target as parameters
    def f(self, nums, target):
        # Initialize a dictionary to store the prefix sums and their frequencies
        d = {}
        d[0] = 1
        # Initialize the current sum and the count to zero
        s = 0
        cnt = 0
        for x in nums:
            s += x
            cnt += d.get(s - target, 0)
            d[s] = d.get(s, 0) + 1
        return cnt
