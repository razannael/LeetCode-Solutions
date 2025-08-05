class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:

        n = len(nums)

        max_decreasing_sum = [0]*n
        max_increasing_sum = [0]*n

        max_decreasing_sum[0] = nums[0]
        max_increasing_sum[-1] = nums[-1]

        for i in range(1, n):
            if nums[i] > nums[i-1]:
                max_decreasing_sum[i] = max(max_decreasing_sum[i-1] + nums[i], nums[i])
            else:
                max_decreasing_sum[i] = nums[i]

        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                max_increasing_sum[i] = max(max_increasing_sum[i+1] + nums[i], nums[i])
            else:
                max_increasing_sum[i] = nums[i]
                

        i = 0
        ans = float("-inf")
        
        while i < n:
            
            if i+2 < n and nums[i] < nums[i+1] and nums[i+1] > nums[i+2]:
                cur_sum = 0
                
                j = i+1
                while j + 1 < n and nums[j] > nums[j+1]:
                    cur_sum += nums[j]
                    j+=1

                if j+1  < n and nums[j] < nums[j+1]:
                    cur_sum += nums[j]
                    ans = max(ans, max_decreasing_sum[i] + cur_sum + max_increasing_sum[j+1])

                i = j-1

            i+=1

        return ans
                    
                