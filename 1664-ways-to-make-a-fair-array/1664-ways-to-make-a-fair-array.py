class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        total_even, total_odd = 0, 0
        for i, num in enumerate(nums):
            if i % 2 == 0:
                total_even += num
            else:
                total_odd += num

        count = 0
        left_even = left_odd = 0

        for i, num in enumerate(nums):
            if i % 2 == 0:
                total_even -= num
            else:
                total_odd -= num

            # After removal, elements to the right shift left,
            # so their parity flips.
            if left_even + total_odd == left_odd + total_even:
                count += 1

            # Add current element to left prefix sums
            if i % 2 == 0:
                left_even += num
            else:
                left_odd += num

        return count