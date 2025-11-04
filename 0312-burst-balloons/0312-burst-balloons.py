class Solution:
    def maxCoins(self, nums: List[int]) -> int:

        nums.insert(0,1)
        nums.append(1)

        def recursive(i, j, memo):
            if i == j:
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            max_cost = float('-inf')
            for k in range(i, j):
                curr_cost = nums[i-1] * nums[k] * nums[j]
                left_cost = recursive(i, k, memo)
                right_cost = recursive(k+1, j, memo)
                max_cost = max(max_cost, curr_cost + left_cost + right_cost)
            memo[(i,j)] = max_cost
            return max_cost
        
        memo = {}
        return recursive(1, len(nums)-1, memo)
        