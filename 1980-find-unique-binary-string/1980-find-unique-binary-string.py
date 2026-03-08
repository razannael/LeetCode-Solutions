class Solution:
    def findDifferentBinaryString(self, nums: list[str]) -> str:
        
        flip = lambda x: '0' if x=='1' else '1'
        return ''.join(map(flip,[nums[i][i] for i in range(len(nums))]))
    