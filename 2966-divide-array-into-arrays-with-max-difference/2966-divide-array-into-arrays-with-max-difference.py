class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(0, len(nums), 3):
            sub = nums[i:i+3]
            if sub[-1] - sub[0] <= k:
                ans.append(sub)
            else:
                return []
        return ans
