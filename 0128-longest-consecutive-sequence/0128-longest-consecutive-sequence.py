class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_set = set(nums)
        length = 0
        for num in my_set:
            if num-1 not in my_set:
                end = num+1
                while end in my_set:
                    end +=1
                length = max(length, end-num)
        return length