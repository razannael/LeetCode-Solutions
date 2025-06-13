class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        def isValid(mid):
            count, i = 0, 0
            while i < len(nums) - 1:
                if nums[i + 1] - nums[i] <= mid:
                    count += 1
                    i += 2
                else:
                    i += 1
            return count >= p

        l, r = 0, nums[-1] - nums[0]
        res = float('inf')
        while l <= r:
            mid = (l + r) // 2
            if isValid(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res