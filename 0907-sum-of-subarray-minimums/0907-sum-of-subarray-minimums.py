class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        stack = []  # Monotonic stack to store indices
        
        # Initialize arrays to store the left and right boundaries of the minimum element for each index
        left_boundary = [0] * len(arr)
        right_boundary = [0] * len(arr)
        
        # Calculate the left boundaries
        for i in range(len(arr)):
            while stack and arr[i] < arr[stack[-1]]:
                stack.pop()
            left_boundary[i] = stack[-1] + 1 if stack else 0
            stack.append(i)
        
        # Clear the stack for the next step
        stack = []
        
        # Calculate the right boundaries
        for i in range(len(arr) - 1, -1, -1):
            while stack and arr[i] <= arr[stack[-1]]:
                stack.pop()
            right_boundary[i] = stack[-1] - 1 if stack else len(arr) - 1
            stack.append(i)
        
        # Calculate the sum of minimums for each subarray
        result = 0
        for i in range(len(arr)):
            result = (result + arr[i] * (i - left_boundary[i] + 1) * (right_boundary[i] - i + 1)) % MOD
        
        return result