class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums) - 1
        print(f"Value of n: {n}")
        test_set = set()
        num_n = 0 

        for num in nums:
            if num > n:
                return False
            if num == n:
                num_n += 1
                if num_n > 2:
                    return False
                continue

            if num in test_set:
                return False 
            
            test_set.add(num)

        return num_n == 2