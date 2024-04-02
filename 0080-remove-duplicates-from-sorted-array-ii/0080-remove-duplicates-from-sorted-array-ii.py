class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        my_Dict = {}
        for num in nums:
            if num in my_Dict:
                my_Dict[num] += 1
            else:
                my_Dict[num] = 1
        for key in my_Dict:
            while my_Dict[key] > 2:
                nums.remove(key)
                my_Dict[key] -= 1
        return len(nums)