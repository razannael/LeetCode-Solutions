class Solution:

    def maximumPrimeDifference(self, nums: List[int]) -> int:

        def isPrime(num):
            if num < 4: return num > 1
            for i in range(2,isqrt(num)+1):
                if num % i == 0: return False
            return True

        def findPrime():
            for i, num in enumerate(nums):
                if isPrime(num): return i
                  

        left = findPrime()
        nums = nums[::-1]
        rght = len(nums)-1 - findPrime()
        return abs(rght - left)