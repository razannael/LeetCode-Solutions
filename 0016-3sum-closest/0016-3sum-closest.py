class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        result = nums[0] + nums[1] + nums[2]

        for i in range(len(nums)):
            if nums[i] == nums[i - 1]:
                continue

            j = i + 1
            k = len(nums) - 1

            while j < k:
                trip_sum = nums[i] + nums[j] + nums[k]

                if abs(target - trip_sum) < abs(target - result):
                    result = trip_sum
                elif trip_sum == target:
                    return target
                elif trip_sum < target:
                    j += 1
                else:
                    k -= 1

        return result