class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        r1 = m-1
        r2 = n-1
        rf = m+n-1
        while r2 >= 0:
            if r1 >= 0 and nums1[r1] > nums2[r2]:
                nums1[rf] = nums1[r1]
                r1-=1
            else:
                nums1[rf] = nums2[r2]
                r2-=1
            rf-=1