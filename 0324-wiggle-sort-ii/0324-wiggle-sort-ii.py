# Inspired by https://leetcode.com/problems/wiggle-sort-ii/discuss/77677/O(n)%2BO(1)-after-median-Virtual-Indexing
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        mid = len(nums) // 2
        def quickselect(arr, lo, hi, k):
            pivot = random.randint(lo, hi)
            arr[pivot], arr[hi] = arr[hi], arr[pivot]
            pivot = lo
            for i in range(lo, hi):
                if arr[i] < arr[hi]:
                    arr[i], arr[pivot] = arr[pivot], arr[i]
                    pivot += 1
            arr[pivot], arr[hi] = arr[hi], arr[pivot]
            if k == pivot:
                return arr[pivot]
            elif k < pivot:
                return quickselect(arr, lo, pivot-1, k)
            else:
                return quickselect(arr, pivot+1, hi, k)
        median = quickselect(nums, 0, len(nums)-1, mid)
                    
        # virtual index
        vi = lambda x: x * 2 + 1 if x < mid else (x - mid) * 2
        i, j, k = 0, 0, len(nums) - 1
        while j <= k:
            if nums[vi(j)] < median:
                nums[vi(j)], nums[vi(k)] = nums[vi(k)], nums[vi(j)]
                k -= 1
            elif nums[vi(j)] > median:
                nums[vi(j)], nums[vi(i)] = nums[vi(i)], nums[vi(j)]
                i += 1
                j += 1
            else:
                j += 1