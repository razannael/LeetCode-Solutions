class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        res, stack = [], []
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return False
            if nums[i] > nums[i - 1]:
                res.append(True)
            else:
                res.append(False)
        print(res)
        for i in res:
            if stack and stack[-1] == i:
                continue
            stack.append(i)
        return stack == [True, False, True]