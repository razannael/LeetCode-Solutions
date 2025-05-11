class Solution(object):
    def minSum(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        sum1, sum2 = 0, 0
        zeros1, zeros2 = 0, 0

        for num in nums1:
            if num == 0:
                zeros1 += 1
            sum1 += num

        for num in nums2:
            if num == 0:
                zeros2 += 1
            sum2 += num

        if zeros1 == 0 and zeros2 == 0:
            return sum1 if sum1 == sum2 else -1
        elif zeros1 == 0:
            return sum1 if sum2 + zeros2 <= sum1 else -1
        elif zeros2 == 0:
            return sum2 if sum1 + zeros1 <= sum2 else -1

        return max(sum1 + zeros1, sum2 + zeros2)