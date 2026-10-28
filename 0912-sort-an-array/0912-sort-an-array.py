class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # using radix sort
        def radixSort(nums):
            if nums == []:
                return []
            radixArray = [[] for i in range(10)]
            maxValue = max(nums)
            exp = 1
            while (maxValue // exp) > 0:
                while len(nums) != 0:
                    ln = nums.pop()  # last number
                    d = (ln // exp) % 10
                    radixArray[d].append(ln)
                for arr in radixArray:
                    while len(arr) != 0:
                        nums.append(arr.pop())
                exp = exp * 10
            return nums
        left = []
        right = []
        for i in nums:
            if i < 0:
                left.append(-1*i)
            else:
                right.append(i)
        left = radixSort(left)
        right = radixSort(right)
        neg = [-1*i for i in left[::-1]]
        return neg + right