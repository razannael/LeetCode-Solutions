from typing import List
from collections import defaultdict

class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # Group indices by value
        pos = defaultdict(list)
        for i, val in enumerate(nums):
            pos[val].append(i)
        
        ans = [0] * n
        
        for indices in pos.values():
            m = len(indices)
            if m == 1:
                continue  # ans already 0
            total_sum = sum(indices)
            left_sum = 0  # sum of indices before current i
            for i, idx in enumerate(indices):
                left_count = i
                right_count = m - 1 - i
                right_sum = total_sum - left_sum - idx
                ans[idx] = (left_count * idx - left_sum) + (right_sum - right_count * idx)
                left_sum += idx
        
        return ans