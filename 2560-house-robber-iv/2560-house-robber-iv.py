class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def canSteal(mid):
            count = 0
            taken = False

            for num in nums:
                if taken:
                    taken = False
                elif num <= mid:
                    count += 1
                    taken = True
            
            return count >= k
        
        low, high = min(nums), max(nums)
        while low < high:
            mid = (low + high) //2

            if canSteal(mid):
                high = mid
            else:
                low = mid + 1
        
        return low