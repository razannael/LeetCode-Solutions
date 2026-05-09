from typing import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        answer = [0 for _ in range(len(nums))]

        for i in range(n):
            answer[2*i] = nums[i]
            answer[2*i+1] = nums[n+i]

        return answer